import pytest
from playwright.sync_api import Page, expect
from config.settings import USERNAME, PASSWORD


@pytest.mark.smoke
def test_full_checkout_journey(login_page, inventory_page, cart_page, checkout_page, page: Page):
    login_page.login(USERNAME, PASSWORD)
    inventory_page.add_item("Sauce Labs Backpack")
    inventory_page.open_cart()
    cart_page.checkout()
    checkout_page.fill_details("Tejas", "Patil", "395001")
    page.get_by_test_id("finish").click()
    expect(page.get_by_test_id("complete-header")).to_have_text("Thank you for your order!")