import pytest
from playwright.sync_api import Page
from config.settings import BASE_URL
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1280, "height": 720}}


@pytest.fixture(autouse=True)
def set_test_id(playwright):
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def login_page(page: Page):
    lp = LoginPage(page)
    lp.open(BASE_URL)
    return lp

@pytest.fixture
def inventory_page(page: Page):
    return InventoryPage(page)

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)