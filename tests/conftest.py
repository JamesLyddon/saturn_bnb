import pytest, sys, random, pytest, os
from pathlib import Path
from xprocess import ProcessStarter
from lib.database_connection import DatabaseConnection
from app import app
from playwright.sync_api import Page, expect

# This is a Pytest fixture.
# It creates an object that we can use in our tests.
# We will use it to create a database connection.
@pytest.fixture
def db_connection():
    conn = DatabaseConnection(test_mode=True)
    conn.connect()
    return conn

# This fixture starts the test server and makes it available to the tests.
# You don't need to understand it in detail.
@pytest.fixture
def test_web_address(xprocess):
    python_executable = sys.executable
    app_file = Path(__file__).resolve().parent.parent / 'app.py'
    port = str(random.randint(4000, 4999))
    class Starter(ProcessStarter):
        env = {"PORT": port, "APP_ENV": "test", **os.environ}
        pattern = "Debugger PIN"
        args = [python_executable, app_file]

    xprocess.ensure("flask_test_server", Starter)

    yield f"localhost:{port}"

    xprocess.getinfo("flask_test_server").terminate()


# Now, when we create a test, if we allow it to accept a parameter called
# `db_connection` or `test_web_address`, Pytest will automatically pass in the
# objects we created above.

# For example:

# def test_something(db_connection, test_web_address):
#     # db_connection is now available to us in this test.
#     # test_web_address is also available to us in this test.


# We'll also create a fixture for the client we'll use to make test requests.
@pytest.fixture
def web_client():
    app.config['TESTING'] = True # This gets us better errors
    with app.test_client() as client:
        yield client



@pytest.fixture
def sign_in_user(db_connection, test_web_address, page):
    # we wrap a _login function here, as otherwise the fixture would run as soon as the test starts
    def _login():
        db_connection.seed('seeds/bnb_seed.sql')
        page.goto(f'http://{test_web_address}/login')
        page.fill('input[name=username]', 'janesmith')
        page.fill('input[name=password]', 'SuperSecret999')
        page.click('button[type=submit]')
        
    return _login