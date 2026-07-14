import re

import allure
from playwright.sync_api import Page

from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage


class CreateCourseToolbarViewComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Create course toolbar title')
        self.create_course_toolbar_button = Button(page, 'create-course-toolbar-create-course-button', 'Create course toolbar button')

    @allure.step('Check visible create course toolbar component')
    def check_visible(self, is_create_course_disabled: bool=True):
        self.title.check_visible()
        self.title.check_have_text('Create course')

        self.create_course_toolbar_button.check_visible()
        if is_create_course_disabled:
            self.create_course_toolbar_button.check_disabled()
        else:
            self.create_course_toolbar_button.check_enabled()

    def click_create_course_button(self):
        self.create_course_toolbar_button.click()
        self.check_current_url(re.compile(".*/#/courses"))