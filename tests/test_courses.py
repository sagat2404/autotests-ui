from playwright.sync_api import expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    expect_text_on_toolbar_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(expect_text_on_toolbar_title).to_be_visible()
    expect(expect_text_on_toolbar_title).to_have_text('Courses')

    expect_text_on_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(expect_text_on_title).to_be_visible()
    expect(expect_text_on_title).to_have_text('There is no results')

    expect_text_on_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(expect_text_on_icon).to_be_visible()

    expect_text_on_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(expect_text_on_description).to_be_visible()
    expect(expect_text_on_description).to_have_text('Results from the load test pipeline will be displayed here')
