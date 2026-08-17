from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://playwright.org/", wait_until='networkidle')

    text = ''

    page.evaluate(
        """
        
        """
    )
