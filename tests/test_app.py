from playwright.sync_api import Page, expect
import pytest
from app import app

# Tests for your routes go here
@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


"""
Tests for new user sign up page
"""
def test_get_signup_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/register")

    h1_tag = page.locator(".t-headline")
    expect(h1_tag).to_have_text("Register")

    label_tag = page.locator("label.label").nth(0)
    expect(label_tag).to_have_text("Username")
    
    label_tag = page.locator("label.label").nth(1)
    expect(label_tag).to_have_text("First Name")
    
    label_tag = page.locator("label.label").nth(2)
    expect(label_tag).to_have_text("Last Name")
    
    label_tag = page.locator("label.label").nth(3)
    expect(label_tag).to_have_text("Password")
    
    label_tag = page.locator("label.label").nth(4)
    expect(label_tag).to_have_text("Email")
    
    label_tag = page.locator("label.label").nth(5)
    expect(label_tag).to_have_text("Phone Number")
    
    button_tag = page.locator("button")
    expect(button_tag).to_have_text("Register")


def test_user_registration_successful(client):
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



"""
We can render the spaces page with all spaces from the database
"""
def test_get_spaces(page, test_web_address, db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    page.goto(f"http://{test_web_address}/spaces")
    
    headline = page.locator(".t-headline")
    sub_heading = page.locator(".t-sub-heading")
    create_space_btn = page.locator(".t-create-space-btn")
    
    space_titles = page.locator(".t-space-title")
    first_title = space_titles.first
    last_title = space_titles.last
    space_addresses = page.locator(".t-space-address")
    first_address = space_addresses.first
    last_address = space_addresses.last
    
    expect(headline).to_have_text("Available Spaces")
    expect(sub_heading).to_have_text("Find your perfect stay.")
    expect(create_space_btn).to_have_text("Create Space")
    
    expect(space_titles).to_have_count(5)
    expect(space_addresses).to_have_count(5)
    
    expect(first_title).to_have_text("Cozy Apartment in Ce...")
    expect(last_title).to_have_text("Rustic Cottage in Sc...")

    expect(first_address).to_have_text("10 Downing St, Londo...")
    expect(last_address).to_have_text("Loch Ness Road, Inve...")