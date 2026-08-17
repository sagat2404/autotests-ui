from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://playwright.org/")

    email_input = page.locator('')
    email_input.fill("user@user.ru")

    password_input = page.get_by_test_id('input[type="password"]').locator('input')
    password_input.fill("password")

    login_button = page.locator('button[type="submit"]')
    login_button.click()

    wrong_email_or_password = page.get_by_test_id('input[type="email"]')
    expect(wrong_email_or_password).to_be_visible()
    expect(wrong_email_or_password).to_have_text('')

    page.wait_for_timeout(5000)