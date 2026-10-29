from playwright.sync_api import Page, expect
from config.settings import USERNAME, PASSWORD


def test_valid_login(login_page, page: Page):
    login_page.login(USERNAME, PASSWORD)
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test='title']")).to_have_text("Products")