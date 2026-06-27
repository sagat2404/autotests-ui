from playwright.sync_api import Page

from elements.input import Input
from pages.base_page import BasePage


class RegistrationFormComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email = Input(page, 'registration-form-email-input', 'Registration email')
        self.username = Input(page, 'registration-form-username-input', 'Registration username')
        self.password = Input(page, 'registration-form-password-input', 'Registration password')

    def fill(self, email: str, username: str, password: str):
        self.email.fill(email)
        self.username.fill(username)
        self.password.fill(password)

    def check_visible(self, email: str, username: str, password: str):
        self.email.check_have_value(email)
        self.username.check_have_value(username)
        self.password.check_have_value(password)
