import os
# ==== packages ====
from flask import Flask, request, render_template, url_for, redirect
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
<<<<<<< HEAD
from lib.booking import Booking
from lib.booking_repository import BookingRepository
=======
from lib.request_repository import RequestRepository

>>>>>>> main

# ==== Set up ====
# Create a new Flask app
app = Flask(__name__)

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

# ==== Register, Login, Logout, Dashboard Routes ====
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
                    return redirect(url_for('get_all_spaces'))

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
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

    return redirect('/spaces')

# ==== Requests Routes ====
@app.route('/requests', methods=['GET'])
@login_required
def get_all_requests():
    connection = get_flask_database_connection(app)
    requests_repo = RequestRepository(connection)
    requests = requests_repo.all()
    
    return render_template('requests.html', requests=requests)

@app.route('/spaces/<int:id>', methods=["GET"])
def get_space_with_id(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)

    space = repo.find(id)

    return render_template('/spaces/show.html', space = space)

@app.route('/spaces/<int:id>', methods=["POST"])
def handle_booking_request(id):
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    date = request.form['date']
    space_id = id

    repo = SpaceRepository(connection)

    space = repo.find(id)

    is_available = booking_repo.is_available(date, space_id)

    if is_available:
        redirect('/requests')
    else:
        return render_template('/spaces/show.html', space = space, rejection_message = 'Dates not available')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

