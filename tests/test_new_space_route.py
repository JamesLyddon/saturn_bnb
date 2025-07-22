from playwright.sync_api import Page, expect

def test_get_form(page, test_web_address):
    page.goto(f'http://{test_web_address}/spaces/new')
    list_labels = page.locator('label')

    expect(list_labels).to_have_text(["Title", "Description", "Price", "Address"])

def test_create_new_space(db_connection, page, test_web_address):
    db_connection.seed('seeds/bnb_seed.sql')
    page.goto(f'http://{test_web_address}/spaces/new')

    page.fill("input[name=title]", 'a lovely house in newcastle')
    page.fill("input[name=description]", '5 bedroom house with pool')
    page.fill("input[name=price]", '100')
    page.fill("input[name=address]", '124 Oxford Street')

    page.click("text=Create Space")

    spaces_titles = page.locator(".t-space-title")

    expect(spaces_titles).to_have_text(["Cozy Apartment in Ce...", "Spacious Family Home...", 'Beachfront Villa wit...', 'Charming Edinburgh L...', 'Rustic Cottage in Sc...', 'a lovely house in ne...'])