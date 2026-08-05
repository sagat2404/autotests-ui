import pytest
from playwright.sync_api import Playwright, Page

from config import settings
from tools.routes import AppRoute


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    page.goto(AppRoute.REGISTRATION)

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(settings.test_user.email)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(settings.test_user.username)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(settings.test_user.password)

    register_button = page.get_by_test_id('registration-page-registration-button')
    register_button.click()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture(scope="function")
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page
    browser.close()


@pytest.fixture(scope="function")
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    yield page
    browser.close()