from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://playwright.org/')

    login_button = page.get_by_test_id('')
    expect(login_button).to_be_disabled()