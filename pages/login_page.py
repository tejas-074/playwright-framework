from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_test_id("username")
        self.password = page.get_by_test_id("password")
        self.login_button = page.get_by_test_id("login-button")

    def open(self, base_url):
        self.page.goto(base_url)

    def login(self, user, pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()