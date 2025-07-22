from playwright.sync_api import Page, expect
import pytest
from app import app

# Tests for your routes go here
@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    p_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("This is the homepage.")

def test_get_signup_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/register")

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Register a new user")
    
    label_tag = page.locator("label").nth(0)
    expect(label_tag).to_have_text("User name:")
    
    label_tag = page.locator("label").nth(1)
    expect(label_tag).to_have_text("First name:")
    
    label_tag = page.locator("label").nth(2)
    expect(label_tag).to_have_text("Last name:")
    
    label_tag = page.locator("label").nth(3)
    expect(label_tag).to_have_text("Password:")
    
    label_tag = page.locator("label").nth(4)
    expect(label_tag).to_have_text("Email:")
    
    label_tag = page.locator("label").nth(5)
    expect(label_tag).to_have_text("Phone number:")

    button_tag = page.locator("button")
    expect(button_tag).to_have_text("Submit")

def test_register_success(client):
    response = client.post('/register', data={
        'username': 'Saima1',
        'first_name': 'Saima',
        'last_name': 'Abdus',
        'password': 'saima123',
        'email': 'saima@email.com',
        'phone_number': '01234567890',
    })
    assert response.status_code == 200
    assert f"User succesfully registered!"



# def test_post_new_user(page, test_web_address):
#     page.goto(f"http://{test_web_address}/register")
