from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')

        self.title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_course_exercises_toolbar_button = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Exercises')
        expect(self.create_course_exercises_toolbar_button).to_be_visible()
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )

    def click_create_exercise_button(self):
        self.create_course_exercises_toolbar_button.click()