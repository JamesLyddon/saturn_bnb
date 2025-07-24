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
Tests for sign-in page
"""
def test_get_signin_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    
    h1_tag = page.locator(".t-headline")
    expect(h1_tag).to_have_text("Login")
    
    label_tag = page.locator("label.label").nth(0)
    expect(label_tag).to_have_text("Username")
    
    label_tag = page.locator("label.label").nth(1)
    expect(label_tag).to_have_text("Password")
    
def test_user_signin_successfully(client):
        response = client.post('/login', data={
            'username': 'Saima1',
            'password': 'saima123',
        })
        assert response.status_code == 200
        assert f"Logged in, welcome back Saima1', 'success'"
    


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

"""
Tests for the request page routes 
"""
def test_get_request_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/bnb_seed.sql")
    page.goto(f"http://{test_web_address}/login")
    page.fill('input[name="username"]', 'janesmith')
    page.fill('input[name="password"]', 'SuperSecret999')
    page.click('button[type="submit"]')
    
    page.goto(f"http://{test_web_address}/requests")
    print("request page")
    
    h2_tag = page.locator("h2", has_text="Bookings Received")
    expect(h2_tag).to_have_text("Bookings Received")
    
    div_tag = page.locator(".t-approve-btn")
    expect(div_tag).to_have_text("Approve")
    expect(div_tag).to_be_visible()

    div_tag = page.locator(".t-reject-btn")
    expect(div_tag).to_have_text("Reject")
    expect(div_tag).to_be_visible()


def test_post_approve_request(page, sign_in_user, test_web_address, db_connection):
    db_connection.seed("seeds/bnb_seed.sql")

    sign_in_user()

    page.goto(f"http://{test_web_address}/requests")
    page.click('form[action="/requests/2/confirmed"] button')

    result = db_connection.execute("SELECT status FROM bookings WHERE id = 2")
    assert result[0]["status"] == "confirmed"
    
    
def test_post_reject_request(page, sign_in_user, test_web_address, db_connection):
    db_connection.seed("seeds/bnb_seed.sql")

    sign_in_user()

    page.goto(f"http://{test_web_address}/requests")
    page.click('form[action="/requests/2/rejected"] button')

    result = db_connection.execute("SELECT status FROM bookings WHERE id = 2")
    assert result[0]["status"] == "rejected"
    
    



# def test_get_space_with_id(page, test_web_address, db_connection):
#     db_connection.seed("seeds/bnb_seed.sql")
#     page.goto(f"http://{test_web_address}/spaces")

#     space_link = page.locator(".space-1")
#     space_link.click()
    
#     title = page.locator(".space-title")
#     price = page.locator(".space-price")
#     expect(title).to_have_text("Cozy Apartment in Central London")

#     expect(price).to_have_text("£120.00")
