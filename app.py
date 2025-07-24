import os
# ==== packages ====
from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mail import Mail, Message
from lib.database_connection import get_flask_database_connection
from wtforms.validators import ValidationError
from flask_bcrypt import Bcrypt
from lib.forms.register_form import RegisterForm
from lib.forms.login_form import LoginForm
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
# ==== Models & Repos ====
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.user_repository import UserRepository
from lib.user import User
from lib.request_repository import RequestRepository
from lib.booking_repository import BookingRepository

# ==== Set up ====
# Create a new Flask app
app = Flask(__name__)

# initialise flask_mail
mail = Mail(app)

# Password hashing using bycrpt
bycrpt = Bcrypt(app)

# Example for development (can go through setting up a .env file together later)
app.config['SECRET_KEY'] = 'supersecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    user = repo.find(user_id)
    return user

# check username exists
def validate_username(username):
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    users = repo.all()
    username_exists = False
    
    for user in users:
        if user.username == username:
            username_exists = True
    
    if username_exists:
        raise ValidationError(
            'That username already exists. Please choose a different one.')

# ==== Mail setup ====

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'saturnbnb78@gmail.com'
app.config['MAIL_PASSWORD'] = 'SuperSecret999'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True

# ==== Register, Login, Logout Routes ====
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        users = repo.all()
    
        for user in users:
            if user.username == form.username.data:
                if bycrpt.check_password_hash(user.password, form.password.data):
                    login_user(user)
                    flash(f'Logged in, welcome back {current_user.first_name}', 'success')
                    return redirect(url_for('get_all_spaces'))

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash(f'You are now logged out', 'success')
    return redirect(url_for('get_all_spaces'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data)
        hashed_password_string = hashed_password.decode('utf-8')
        new_user = User(None, username=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data, password=hashed_password_string, email=form.email.data, phone_number=form.phone_number.data)
    
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        
        repo.create(new_user)
        flash(f'Account created, welcome {form.first_name.data}! Now login to continue', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

# ==== Spaces Routes ====
@app.route('/', methods=['GET'])
@app.route('/spaces', methods=['GET'])
def get_all_spaces():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.all()
    return render_template('spaces.html', spaces=spaces)

@app.route('/spaces/new', methods=["GET"])
@login_required
def get_new_space():
    return render_template('spaces/new.html')

@app.route('/spaces', methods=["POST"])
@login_required
def create_space():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)

    # get fields from request form
    title = request.form['title']
    description = request.form['description']
    price = request.form['price']
    address = request.form['address']
    host_id = current_user.id

    space = Space(None, host_id, title, description, price, address)

    repo.create(space)
    flash(f'Your "{title}" space has been successfully listed!', 'success')

    return redirect('/spaces')

# ==== Requests Routes ====
@app.route('/requests', methods=['GET'])
@login_required
def get_all_requests():
    connection = get_flask_database_connection(app)
    requests_repo = RequestRepository(connection)
    requests = requests_repo.all()
    
    return render_template('requests.html', requests=requests)

@app.route('/requests/<int:booking_id>/<action>', methods=['POST'])
@login_required
def approve_reject_request(booking_id, action):
    actions = ['confirmed', 'rejected']
    if action not in actions:
        flash('Invalid action', 'danger')
        return redirect(url_for('get_all_requests'))
    
    connection = get_flask_database_connection(app)
    
    bookings_repo = BookingRepository(connection)
    booking = bookings_repo.find(booking_id)
    
    # make sure the booking still exists
    if not booking:
        flash('Booking not found.', 'danger')
        return redirect(url_for('get_all_requests'))
    
    space_repo = SpaceRepository(connection)
    space = space_repo.find(booking.space_id)
    
    # make sure the current_user is the host/owner of the space
    if not space or space.host_id != current_user.id:
        flash('You are not authorized to reject this booking', 'danger')
        return redirect(url_for('get_all_requests'))
    
    # change booking status based on action
    bookings_repo.update_status(booking_id, action)
    
    flash_category = 'success' if action == 'confirmed' else 'danger'
    
    # search for similar pending requests and auto reject them
    if action == 'confirmed':
        bookings_repo.reject_similar_pending(
            confirmed_space_id=booking.space_id,
            confirmed_date=booking.date,
            confirmed_booking_id=booking.id
        )
        flash(f'Booking {action}! Any similar requests rejected', flash_category)
    else:
        flash(f'Booking {action}!', flash_category)
        
        
        # all_bookings = bookings_repo.all()
        # for item in all_bookings:
        #     if item.id == booking.id:
        #         continue
        #     if item.space_id == booking.space_id and item.date == booking.date and item.status == 'pending':
                # bookings_repo.update_status(item.id, 'rejected')
    
    # Add logic here to send emails
    #
    #
    
    
    return redirect(url_for('get_all_requests'))


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

