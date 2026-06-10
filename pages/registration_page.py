from playwright.sync_api import Page, expect


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.click_registration_button = page.get_by_test_id('registration-page-registration-button')

    def visit(self, url: str):
        self.page.goto(url, wait_until='networkidle')

    def fill_registration_form(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_button(self):
        self.click_registration_button.click()
