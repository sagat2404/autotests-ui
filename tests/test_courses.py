from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        register_button = page.get_by_test_id('registration-page-registration-button')
        register_button.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        expect_text_on_toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(expect_text_on_toolbar_title).to_be_visible()
        expect(expect_text_on_toolbar_title).to_have_text('Courses')

        expect_text_on_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(expect_text_on_title).to_be_visible()
        expect(expect_text_on_title).to_have_text('There is no results')

        expect_text_on_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(expect_text_on_icon).to_be_visible()

        expect_text_on_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(expect_text_on_description).to_be_visible()
        expect(expect_text_on_description).to_have_text('Results from the load test pipeline will be displayed here')
