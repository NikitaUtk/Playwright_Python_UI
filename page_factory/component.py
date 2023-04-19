from abc import ABC, abstractmethod

import allure
from playwright.sync_api import Locator, Page, expect
from playwright.async_api import Page

class Component(ABC):
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page = page
        self.name = name
        self.locator = locator

    @property
    @abstractmethod
    def type_of(self) -> str:
        return 'component'

    def get_all_elements(self, **kwargs) -> list:
        locator = self.locator.format(**kwargs)
        self.wait_loading()
        return self.page.query_selector_all(locator)

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        self.wait_loading()
        return self.page.locator(locator)

    def get_locator_without_wait(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.locator(locator)

    def get_locator_by_text(self, keyword: str, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.locator(locator).get_by_text(keyword)

    def go_back(self):
        self.page.go_back()

    def check_checkbox(self,keyword: str, **kwargs) -> bool:
        locator = self.locator.format(**kwargs)
        self.wait_loading()
        checkbox = self.page.get_by_label(keyword).first
        return checkbox.is_checked()

    def get_ch_locator(self, keyword: str, **kwargs) -> Locator:
        self.wait_loading()
        return self.page.locator(keyword)

    def click(self, enter=False, **kwargs) -> None:
        with allure.step(f'Clicking {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(**kwargs)
            self.wait_loading()
            locator.click()
            if enter:
                locator.press('Enter')

    def click_first_page(self, enter=False, **kwargs) -> None:
        with allure.step(f'Clicking {self.type_of} with name "{self.name}"'):
            locator = self.get_locator_without_wait(**kwargs)
            locator.click()
            if enter:
                locator.press('Enter')

    def click_by_text(self,keyword: str, **kwargs) -> None:
        with allure.step(f'Clicking {self.type_of} with text "{self.name}"'):
            locator = self.get_locator_by_text(keyword,**kwargs)
            locator.click()

    def should_be_visible(self, **kwargs) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.name}" is visible'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_be_visible()

    def should_have_text(self, text: str, **kwargs) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.name}" has text "{text}"'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_text(text)

    def is_visible(self, **kwargs) -> bool:
        with allure.step(f'Checking that {self.type_of} "{self.name}" is visible'):
            locator = self.get_locator(**kwargs)
            return locator.is_visible()

    def is_enable(self, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is enable'):
            locator = self.get_locator(**kwargs)
            return self.page.is_enabled(locator)

    def wait_for_selector(self,loc:str,**kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is enable'):
            self.page.wait_for_selector(loc)

    def wait_loading(self):
        with allure.step(f'Wait loading'):
            locator = self.page.locator(".ant-spin-spinning")
            try:
                expect(locator).to_be_hidden(timeout=30000)
            except AssertionError:
                print()