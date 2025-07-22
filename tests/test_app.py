from playwright.sync_api import Page, expect

# Tests for your routes go here

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