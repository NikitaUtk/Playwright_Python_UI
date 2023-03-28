import allure
from playwright.sync_api import Page

from page_factory.component import Component
from playwright.sync_api import expect
import re

class ListItem(Component):
    @property
    def type_of(self) -> str:
        return 'list item'

    def compareList(self, value: list, validate_value=True, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):
            locator = self.get_locator(**kwargs)
            locator.all_text_contents()
            if validate_value:
                self.should_have_value(value, **kwargs)


    def should_have_value(self, value: list, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has a value "{value}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_text(value)

    def checkRole(self, value: str, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):
            locator = self.get_locator(**kwargs)
            locator.text_content()

    def listofElements(self, **kwargs) -> list:
        with allure.step(f'Fill {self.type_of} "{self.name}"'):
            return self.get_all_elements(**kwargs)

    def countRow(self, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.name}"'):
            return len(self.get_all_elements(**kwargs))

    def empty_column(self, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.name}"'):
            print(1)