import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(scope='module')
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=['--disable-blink-features=AutomationControlled'])
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope='module')
def credentials():
    return {
        'email': os.getenv('EMAIL'),
        'password': os.getenv('PASSWORD'),
        'contact_email': os.getenv('CONTACT_EMAIL')
    }