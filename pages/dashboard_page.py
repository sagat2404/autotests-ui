from playwright.sync_api import Page, expect


class DashboardPage:
    def __init__(self, page: Page):
        self.expect_text_on_dashboard = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_visible_dashboard_text(self):
        expect(self.expect_text_on_dashboard).to_be_visible()
        expect(self.expect_text_on_dashboard).to_have_text('Dashboard')
