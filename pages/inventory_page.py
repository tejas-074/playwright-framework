from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.get_by_test_id("title")
        self.cart_link = page.get_by_test_id("shopping-cart-link")
        self.cart_badge = page.get_by_test_id("shopping-cart-badge")

    def add_item(self, item_name):
        item = self.page.locator(".inventory_item").filter(has_text=item_name)
        item.get_by_role("button", name="Add to Cart").click()

    def open_cart(self):
        self.cart_link.click()