from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://playwright.org/")
    email_input = page.locator('')
    email_input.focus()

    for char in 'user_mail@mail.ru':
        page.keyboard.type(char)

    page.keyboard.press('ControlOrMeta+A')

