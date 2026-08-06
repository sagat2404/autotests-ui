import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from config import settings, Browser
from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page
from tools.routes import AppRoute


@pytest.fixture(scope="session", params=settings.browsers)
def initialize_browser_state(request: SubRequest, playwright: Playwright) -> Browser:
    browser_type = request.param

    state_file = str(settings.browser_state_file).replace(".json", f"_{browser_type}.json")

    browser = getattr(playwright, browser_type).launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password
    )
    registration_page.click_button()

    context.storage_state(path=state_file)
    browser.close()

    return browser_type


@pytest.fixture()
def chromium_page_with_state(initialize_browser_state: Browser, request: SubRequest, playwright: Playwright) -> Page:
    state_file = str(settings.browser_state_file).replace(".json", f"_{initialize_browser_state}.json")

    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=state_file,
        browser_type=initialize_browser_state
    )


@pytest.fixture(params=settings.browsers)
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, browser_type=request.param)
