import os
from flask import Flask, request, render_template, url_for, redirect
from lib.database_connection import get_flask_database_connection
from wtforms.validators import ValidationError
from lib.dummy_user import Dummy
from lib.dummy_user_repo import DummyRepo
from flask_bcrypt import Bcrypt
from lib.forms.register_form import RegisterForm
from lib.forms.login_form import LoginForm

# Create a new Flask app
app = Flask(__name__)

# Password hashing
bycrpt = Bcrypt(app)

# Example for development
app.config['SECRET_KEY'] = 'supersecretkey'

# check username exists
def validate_username(username):
    connection = get_flask_database_connection(app)
    repo = DummyRepo(connection)
    users = repo.all()
    username_exists = False
    
    for user in users:
        if user.username == username:
            username_exists = True
    
    if username_exists:
        raise ValidationError(
            'That username already exists. Please choose a different one.')


# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        hashed_password = bycrpt.generate_password_hash(form.password.data)
        new_user = Dummy(None, username=form.username.data, first_name=form.first_name.data, last_name=form.last_name.data, password=hashed_password, email=form.email.data, phone_number=form.phone_number.data)
    
        connection = get_flask_database_connection(app)
        repo = DummyRepo(connection)
        
        user = repo.create(new_user)
        
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/users', methods=['GET'])
def users():
    connection = get_flask_database_connection(app)
    repo = DummyRepo(connection)
    users = repo.all()
    return render_template('users.html', users=users)
    
    
    
    
    
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
