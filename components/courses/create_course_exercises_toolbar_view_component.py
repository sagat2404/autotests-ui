import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')

        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Create course exercises title')
        self.create_course_exercises_toolbar_button = Button(page, 'create-course-exercises-box-toolbar-title-text', 'Create course exercises title')

    @allure.step('Check visible create course exercises toolbar view')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')
        self.create_course_exercises_toolbar_button.check_visible()
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )

    def click_create_exercise_button(self):
        self.create_course_exercises_toolbar_button.click()