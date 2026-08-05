from playwright.sync_api import sync_playwright, expect

from tools.routes import AppRoute

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(AppRoute.REGISTRATION)

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    register_button = page.get_by_test_id('registration-page-registration-button')
    register_button.click()

    expect_text_on_dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(expect_text_on_dashboard).to_be_visible()
    expect(expect_text_on_dashboard).to_have_text('Dashboard')
