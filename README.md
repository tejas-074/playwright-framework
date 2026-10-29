# Playwright Python Test Framework

![Tests](https://github.com/tejas-074/playwright-framework/actions/workflows/tests.yml/badge.svg)

End-to-end tests for saucedemo.com: login, cart and a full checkout journey.

## Design decisions
- **Page Object Model**: one class per page in `pages/`, so tests read like plain English.
- **Config in one place**: `config/settings.py` holds URLs and credentials, chosen by the `TEST_ENV` variable.
- **Fixtures in `conftest.py`**: page objects are created once and handed to tests.
- **Reporting from day one**: `pytest.ini` writes an HTML report, screenshots and traces on failure.
- **CI**: GitHub Actions runs every push and uploads the report.

## Run locally
```
pip install -r requirements.txt
playwright install chromium
pytest
```