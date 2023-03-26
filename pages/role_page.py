from playwright.sync_api import Page

from page_factory.list_item import ListItem
from pages.base_page import BasePage


class RolesPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.role = ListItem(
            page, locator='.current-role', name='Current Role'
        )

    def role_present(self, role: str):
        # self.language_title.should_be_visible(language=language)
        self.role.should_have_text(
            role.capitalize(), role=role
        )
