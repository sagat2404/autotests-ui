from playwright.sync_api import sync_playwright, expect, Request, Response

def log_request(request: Request):
    ...

def log_response(response: Response):
    ...

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://playwright.org/')

    page.on('requests')