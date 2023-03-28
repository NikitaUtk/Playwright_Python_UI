from playwright.sync_api import Page

from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.title import Title
from page_factory.image import Image
from API import Response as r
from page_factory.button import Button


class SearchModal:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.image_logo = Image(page, locator='', name='Logo is visible')
        self.search_listofbuttons = ListItem(page, locator='.ant-menu-overflow-item', name='List of buttons')
        self.search_listofhandbook = ListItem(page, locator='li.ant-menu-item[data-menu-id*="rc-menu-uuid-"]', name='Test')
        self.table_row = ListItem(page, locator='tr', name='Table row')
        self.search_listofroles = ListItem(page, locator='ul > li', name='Role list')
        self.list_name_table_column = ListItem(page, locator='td.ant-table-cell[data-column-key]', name='Table column')
        # self.list_name_table_row = ListItem(page, locator='tr.ant-table-row[data-row-key]')
        self.button_next = Button(page, locator='.anticon-right', name='Button next')
        # self.list_name_table_column = ListItem(page, locator='tr.ant-table-row[data-row-key]', name='Table column')
        # elements = page.query_selector_all('td.ant-table-cell[data-column-key]')
        # data_column_keys = [el.get_attribute('data-column-key') for el in elements]
        # print(data_column_keys)
        # self.empty_results_title = Title(
        #     page, locator='p.DocSearch-Help', name='Empty results'
        # )
        # self.search_input = Input(
        #     page, locator='#docsearch-input', name='Search docs'
        # )
        # self.search_result = ListItem(
        #     page, locator='#docsearch-item-{result_number}', name='Result item'
        # )

    def modal_is_opened(self):
        self.search_input.should_be_visible()
        self.empty_results_title.should_be_visible()

    def find_result(self, keyword: str, result_number: int) -> None:
        self.search_input.fill(keyword, validate_value=True)
        self.search_result.click(result_number=result_number)

    # def image_is_visible(self):
    #     self.
    def compareListRoles(self):
        roles = r.getResponse(method="api/Roles", typeRequest="GET")
        apiRoles = [i["name"] for i in roles]
        self.search_listofroles.compareList(apiRoles)

    def compareListButtons(self, ButtonsList: list):
        self.search_listofbuttons.compareList(ButtonsList)

    def find_empty_table(self):
        for i in self.search_listofhandbook.listofElements():
            if '/' in i.get_attribute('data-menu-id'):
                print(i.get_attribute('data-menu-id'))
            else:
                i.click()
                if self.table_row.countRow() < 1:
                    print(i.get_attribute('data-menu-id'))

    def find_empty_column(self):
        dictionaries = {}
        while True:
            for column_name in self.list_name_table_column.listofElements():
                if column_name.inner_text()=='':
                    dictionaries.setdefault(column_name.get_attribute('data-column-key'),[])
                    continue
                dictionaries.setdefault(column_name.get_attribute('data-column-key'),[]).append(column_name.inner_text())
            keys_with_value_2 = [key for key, value in dictionaries.items() if value == []]
            if len(keys_with_value_2)<=1:
                break
            self.button_next.click()