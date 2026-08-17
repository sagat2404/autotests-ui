from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('')

    email_input = page.get_by_test_id('').locator('input')
    email_input.fill('')

    username_input = page.get_by_test_id('').locator('input')
    username_input.fill('')

    password_input = page.get_by_test_id('').locator('input')
    password_input.fill('')

    register_button = page.get_by_test_id('registration-page-registration-button')
    register_button.click()

    context.storage_state(path='browser-state.json')

    page.wait_for_timeout(5000)

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('')
