from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class RegistrationFormComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password = page.get_by_test_id('registration-form-password-input').locator('input')

    def fill(self, email: str, username: str, password: str):
        self.email.fill(email)
        self.username.fill(username)
        self.password.fill(password)

    def check_visible(self, email: str, username: str, password: str):
        expect(self.email).to_have_value(email)
        expect(self.username).to_have_value(username)
        expect(self.password).to_have_value(password)
