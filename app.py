import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/spaces', methods=['GET'])
def get_all_spaces():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.all()
    return render_template('spaces.html', spaces=spaces)

@app.route('/register', methods=["GET"])
def get_register():
    return render_template('register.html')

@app.route('/register', methods=["POST"])
def post_register():
    username = request.form.get('username')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('password')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')

    return f"User succesfully registered!", 200

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

