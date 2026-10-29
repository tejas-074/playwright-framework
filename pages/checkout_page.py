from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.get_by_test_id("firstName")
        self.last_name = page.get_by_test_id("lastName")
        self.postal_code = page.get_by_test_id("postalCode")
        self.continue_button = page.get_by_test_id("continue")

    def fill_details(self, first, last, postcode):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postcode)
        self.continue_button.click()