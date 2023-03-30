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

        # self.api_link = Link(page, locator="//a[text()='API']", name='API')
        # self.docs_link = Link(page, locator="//a[text()='Docs']", name='Docs')
        self.role_button = Button(page, locator=".ant-btn.ant-btn-sm.ant-dropdown-trigger.role-dropdown", name='List of roles')

        self.role_link = Button(page, locator='span', name='Current role')
        self.handbook_link = Button(page, locator='a.navigation-menu-item__link[href*= "/dictionaries"]', name='Handbook')
        self.clients_link = Button(page, locator='a.navigation-menu-item__link[href*= "/clients"]', name='Clients')
        self.deals_link = Button(page, locator='a.navigation-menu-item__link[href*= "/deals"]', name='Deals')
        # self.search_listofbuttons = ListItem(page, locator='.ant-menu-overflow-item', name='List of buttons')
        #
        # self.search_listofhandbook = ListItem(page, locator='li.ant-menu-item[data-menu-id*="rc-menu-uuid-"]', name='Test')
        self.table_row = ListItem(page, locator='tr', name='Table row')

        # self.handbook_test = Link(page, locator=f'li.ant-menu-item[data-menu-id*="DEAL_TYPES"]', name='Test')
        # li.ant - menu - item - selected[data - menu - id = "rc-menu-uuid-12668-8-BUSINESS_SEGMENTS"]


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

    # def open_search(self):
    #     # self.search_button.should_be_visible()
    #     # self.search_button.hover()
    #     self.search_button.click()
    #     # self.search_modal.modal_is_opened()
    #     # self.search_list.should_be_visible()


    def open_roleList(self):
        self.role_button.should_be_visible()
        self.role_button.hover()
        self.role_button.click()

    # def compareListRoles(self):
    #     roles = r.getResponse(method="api/Roles", typeRequest="GET")
    #     apiRoles = [i["name"] for i in roles]
    #     self.search_listofroles.compareList(apiRoles)
    #
    # def compareListButtons(self):
    #     self.search_listofbuttons.compareList(['Отчеты', 'Сделки', 'Контрагенты', 'Справочники', ''])


    # def compare_listhandbook(self):
    #     for i in self.search_listofhandbook.listofElements():
    #         if '/' in i.get_attribute('data-menu-id'):
    #             print(i.get_attribute('data-menu-id'))
    #         else:
    #             i.click()
    #             if self.table_row.countRow() < 1:
    #                 print(i.get_attribute('data-menu-id'))

    # def buttonclick(self):
