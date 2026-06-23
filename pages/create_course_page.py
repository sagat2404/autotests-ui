from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.create_course_form = CreateCourseFormComponent(page)
        self.toolbar_create_course = CreateCourseToolbarViewComponent(page)
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)
        self.toolbar_create_course_exercises = CreateCourseExercisesToolbarViewComponent(page)
        self.create_course_empty_component = EmptyViewComponent(page, 'create-course-preview')

    def click_delete_exercise_button(self, index: int):
        delete_exercise_button = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        )
        delete_exercise_button.click()

    def check_visible_create_exercise_form(self, index: int, title: str, description: str):
        exercise_subtitle = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-subtitle-text"
        )
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        )
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        expect(exercise_subtitle).to_be_visible()
        expect(exercise_subtitle).to_have_text(f"#{index + 1} Exercise")

        expect(exercise_title_input).to_be_visible()
        expect(exercise_title_input).to_have_value(title)

        expect(exercise_description_input).to_be_visible()
        expect(exercise_description_input).to_have_value(description)

    def fill_create_exercise_form(self, index: int, title: str, description: str):
        exercise_title_input = self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        )
        exercise_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        )

        exercise_title_input.fill(title)
        expect(exercise_title_input).to_have_value(title)

        exercise_description_input.fill(description)
        expect(exercise_description_input).to_have_value(description)
