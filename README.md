# SaturnBNB
A comprenehensive AirBnB like website with a frontend, backend, incorporating authentication, viewing and booking places to stay. 

## Features

### Register/Login
- Users can register and login.

### Authentication
- Only authorised users can add a space. 
- Only authorised book a space.
- Only authorised users can view requests made/recieved.

### Spaces
- Users can view all spaces
- Users can view a singular place with all its details, including name, description and price.

### Requests
- Can request to book a space on a particular day.
- Only request to book a space that isnt already booked.
- See all the requests they have made/received
- Accept or reject requests they have received
- See if their request have been accepted.

### Email notifications
- A user will receive an email notification if they have
    - requested to book a space.
    - received a request to book their space.
    - had their booking request accepted.


## Setup

```shell
# Set up the virtual environment
; python -m venv makersbnb-venv

# Activate the virtual environment
; source makersbnb-venv/bin/activate

# Install dependencies
(makersbnb-venv); pip install -r requirements.txt

# Install the virtual browser we will use for testing
(makersbnb-venv); playwright install
# If you have problems with the above, contact your coach

# Install all node dependancies
(makersbnb-venv); npm install

# Create a test and development database
(makersbnb-venv); createdb saturn_bbn
(makersbnb-venv); createdb saturn_bnb_test

# Open lib/database_connection.py and change the database names
(makersbnb-venv); open lib/database_connection.py

# Run the tests (with extra logging)
(makersbnb-venv); pytest -sv

# Run the app
(makersbnb-venv); python app.py

# Now visit http://localhost:5001/index in your browser

