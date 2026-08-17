from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://playwright.org/')

    registration_link = page.get_by_test_id('')
    registration_link.hover()