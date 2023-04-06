import allure
from playwright.sync_api import Page

from page_factory.component import Component
from playwright.sync_api import expect
import re

class ListItem(Component):
    @property
    def type_of(self) -> str:
        return 'list item'

    def compare_list(self, value: list, validate_value=True, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):
            locator = self.get_locator(**kwargs)
            locator.all_text_contents()
            if validate_value:
                self.should_have_value(value, **kwargs)


    def should_have_value(self, value: list, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has a value "{value}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_text(value)

    def check_role(self, value: str, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):
            locator = self.get_locator(**kwargs)
            locator.text_content()

    def list_of_elements(self, loc='', **kwargs) -> list:
        with allure.step(f'Fill {self.type_of} "{self.name}"'):
            if loc == '':
                return self.get_all_elements(**kwargs)
            else:
                locator = self.get_ch_locator(loc,**kwargs)
                return locator.all_text_contents()

    def count_elements(self, **kwargs):
        with allure.step(f'Count elements "{self.name}"'):
            return len(self.get_all_elements(**kwargs))

    def empty_column(self, **kwargs):
        with allure.step(f'Fill {self.type_of} "{self.name}"'):
            print(1)