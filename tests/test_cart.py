from playwright.sync_api import Page, expect
from config.settings import USERNAME, PASSWORD


def test_add_item_to_cart(login_page, inventory_page, page: Page):
    login_page.login(USERNAME, PASSWORD)
    inventory_page.add_item("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")
    inventory_page.open_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

def test_cart_shows_added_item(login_page, inventory_page, cart_page):
    login_page.login(USERNAME, PASSWORD)
    inventory_page.add_item("Sauce Labs Backpack")
    inventory_page.open_cart()
    expect(cart_page.item_names).to_have_count(1)
    expect(cart_page.item_names).to_have_text("Sauce Labs Backpack")