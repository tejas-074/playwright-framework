import os

ENV = os.getenv("TEST_ENV", "dev")

URLS = {
    "dev": "https://www.saucedemo.com",
    "staging": "https://www.saucedemo.com",
}

BASE_URL = URLS[ENV]
USERNAME = os.getenv("APP_USER", "standard_user")
PASSWORD = os.getenv("APP_PASS", "secret_sauce")