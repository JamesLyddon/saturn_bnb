from playwright.sync_api import Page, expect
import pytest
from app import app

# Tests for your routes go here
@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

# def test_get_signup_page(page, test_web_address):
#     page.goto(f"http://{test_web_address}/register")

#     h2_tag = page.locator("h2")
#     expect(h2_tag).to_have_text("Register a new user")
    
#     label_tag = page.locator("label").nth(0)
#     expect(label_tag).to_have_text("User name:")
    
#     label_tag = page.locator("label").nth(1)
#     expect(label_tag).to_have_text("First name:")
    
#     label_tag = page.locator("label").nth(2)
#     expect(label_tag).to_have_text("Last name:")
    
#     label_tag = page.locator("label").nth(3)
#     expect(label_tag).to_have_text("Password:")
    
#     label_tag = page.locator("label").nth(4)
#     expect(label_tag).to_have_text("Email:")
    
#     label_tag = page.locator("label").nth(5)
#     expect(label_tag).to_have_text("Phone number:")

#     button_tag = page.locator("button")
#     expect(button_tag).to_have_text("Submit")

# def test_register_success(client):
#     response = client.post('/register', data={
#         'username': 'Saima1',
#         'first_name': 'Saima',
#         'last_name': 'Abdus',
#         'password': 'saima123',
#         'email': 'saima@email.com',
#         'phone_number': '01234567890',
#     })
#     assert response.status_code == 200
#     assert f"User succesfully registered!"



# def test_post_new_user(page, test_web_address):
#     page.goto(f"http://{test_web_address}/register")


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
    
    # div_tag = page.locator(".t-pending-btn")
    # expect(div_tag).to_have_text("pending")


    # expect(page.locator("text='pending'")).to_be_visible()
