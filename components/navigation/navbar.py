from playwright.sync_api import Page
from components.modals.search_modal import SearchModal
from page_factory.button import Button
from page_factory.list_item import ListItem
from page_factory.link import Link
from settings import *
from API import Response as r


class Navbar:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.search_modal = SearchModal(page)

        self.role_button = Button(page, locator=".ant-btn.ant-btn-sm.ant-dropdown-trigger.role-dropdown", name='List of roles')
        self.role_link = Button(page, locator='span', name='Current role')
        self.handbook_link = Button(page, locator='a.navigation-menu-item__link[href*= "/dictionaries"]', name='Handbook')
        self.clients_link = Button(page, locator='a.navigation-menu-item__link[href*= "/clients"]', name='Clients')
        self.deals_link = Button(page, locator='a.navigation-menu-item__link[href*= "/deals"]', name='Deals')

        self.table_row = ListItem(page, locator='tr', name='Table row')



    def visit_docs(self):
        self.docs_link.click()

    def visit_api(self):
        self.api_link.click()

    def visit_role_page(self, keyword: str):
        self.role_link.click_by_text(keyword)

    def visit_handbook_page(self):
        self.handbook_link.click()

    def visit_clients_page(self):
        self.clients_link.click()

    def visit_deals_page(self):
        self.deals_link.click()


    def open_roleList(self):
        self.role_button.should_be_visible()
        self.role_button.hover()
        self.role_button.click()