import datetime
import time

from playwright.sync_api import Page

from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.title import Title
from page_factory.image import Image
from API import Response as r
from page_factory.button import Button
import allure
from datetime import datetime
class SearchModal:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.image_logo = Image(page, locator='', name='Logo is visible')

        self.search_listofbuttons = ListItem(page, locator='.ant-menu-overflow-item', name='List of buttons')
        self.search_listofhandbook = ListItem(page, locator='li.ant-menu-item[data-menu-id*="rc-menu-uuid-"]', name='Test')
        self.search_listofroles = ListItem(page, locator='ul > li', name='Role list')
        self.table_row = ListItem(page, locator='tr', name='Table row')
        self.list_name_table_column = ListItem(page, locator='td.ant-table-cell[data-column-key]', name='Table column')
        # self.list_name_table_row = ListItem(page, locator='tr.ant-table-row[data-row-key]')

        self.input_filter_version_date = Input(page, locator='input[id="version_date"]', name='Input filter')
        self.input_filter_shortname = Input(page, locator='input[id="shortName"]', name='Input filter')
        self.input_filter_inn_ogrn_kio = Input(page, locator='input[id="inn_ogrn_kio"]', name='Input filter')
        self.input_filter_modified_date = Input(page, locator='input[id="modified_date"]', name='Input filter')
        self.input_filter_biz_size = Input(page, locator='input[id="bizSizeCD"]', name='Input filter')
        self.input_filter_biz_segment = Input(page, locator='input[id="bizSegmentCD"]', name='Input filter')
        self.input_filter_country = Input(page, locator='input[id="countryCD"]', name='Input filter')
        self.input_filter_kpp = Input(page, locator='input[id="kpp"]', name='Input filter')
        self.input_filter_vzl = Input(page, locator='input[id="flagVZL"]', name='Input filter')
        self.input_filter_byvzl = Input(page, locator='input[id="flagByVZL"]', name='Input filter')
        self.input_filter_ofshore = Input(page, locator='input[id="flagOffshore"]', name='Input filter')
        self.input_filter_deal_type = Input(page, locator='input[id="deal_pnd_types_cd"]', name='Input filter')
        self.input_filter_deal_credit_transh = Input(page, locator='span[title="Кредитная сделка. Транш"]', name='Input filter')
        self.input_filter_currency = Input(page, locator='input[id="currency_cd"]', name='Input filter')
        self.input_filter_deal_sum_from = Input(page, locator='input[id="deal_sum_rur_from"]', name='Input filter')
        self.input_filter_deal_sum_to = Input(page, locator='input[id="deal_sum_rur_to"]', name='Input filter')
        self.input_filter_deal_sign_date_from = Input(page, locator='input[id="contract_sign_date"]', name='Input filter')
        self.input_filter_deal_sign_date_to = Input(page, locator='#root > div > div.layout_contentContainer__2-sNh > div:nth-child(1) > div > form > div > div.ant-row.ant-row-no-wrap.ant-row-space-between > div:nth-child(1) > div:nth-child(5) > div > div > div > div > div > div > div > div > div.ant-picker-input.ant-picker-input-active > input', name='Input filter')
        self.input_filter_deal_shortname = Input(page, locator='input[id="client_short_name"]', name='Input filter')
        self.input_check_vzl = Input(page, locator='.ant-checkbox-input[type="checkbox"]', name='Input filter')
        self.input_check_byvzl = Input(page, locator='.ant-checkbox-input[type="checkbox"]', name='Input filter')
        self.input_check_ofshore = Input(page, locator='.ant-checkbox-input[type="checkbox"]', name='Input filter')


        self.button_next = Button(page, locator='.anticon-right', name='Button next')
        self.button_in = ListItem(page, locator='th.ant-table-cell', name='Button sort')
        self.button_sort = Button(page, locator='#undefined_container > div.ant-table-wrapper.data-table_table__2Dpgt.scrollable-data-table > div > div > div > div > div.ant-table-header > table > thead > tr > th.ant-table-cell.ant-table-column-sort.ant-table-column-has-sorters > div > span.ant-table-column-sorter.ant-table-column-sorter-full > span > span.anticon.anticon-caret-up.ant-table-column-sorter-up.active', name='Button next')
        self.button_search = Button(page, locator='button.ant-btn.ant-btn-primary', name='Button search')
        self.button_clear = Button(page, locator='button.ant-btn', name='Button clear')
        self.button_filter_list = Button(page, locator='#root > div > div.layout_contentContainer__2-sNh > div:nth-child(1) > div > div', name='Button filter list')

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


    def compareListRoles(self):
        roles = r.getResponse(method="api/Roles", typeRequest="GET")
        apiRoles = [i["name"] for i in roles]
        self.search_listofroles.compareList(apiRoles)


    def compareListButtons(self, ButtonsList: list):
        self.search_listofbuttons.compareList(ButtonsList)


    def find_empty_table(self):
        error_list = []
        for i in self.search_listofhandbook.listofElements():
            if '/' in i.get_attribute('data-menu-id'):
                continue
            else:
                i.click()
                if self.table_row.countRow() < 1:
                    error_list.append(f"In the handbook with the name {i.get_attribute('data-menu-id')} no values")
        assert error_list ==[], error_list

    def find_empty_column(self):
        dictionaries = {}
        error_list = []
        while True:
            for column_name in self.list_name_table_column.listofElements():
                if column_name.inner_text() == '':
                    dictionaries.setdefault(column_name.get_attribute('data-column-key'), [])
                    continue
                dictionaries.setdefault(column_name.get_attribute('data-column-key'), []).append(
                    column_name.inner_text())
            keys_with_empty_column = [key for key, value in dictionaries.items() if value == []]
            if len(keys_with_empty_column) <= 1:
                error_list.append(f"Empty cell in column {keys_with_empty_column}")
                break
            self.button_next.click()
            # allure.step('Empty column' + str(keys_with_empty_column))
        assert error_list == [], error_list
        """
        --Возможно понадобится
        column_name_list = []
        for column_name in self.list_name_table_column.listofElements():
            if column_name.get_attribute('data-column-key') not in column_name_list:
                column_name_list.append(column_name.get_attribute('data-column-key'))
        empty_column = []
        # for cell_name in column_name_list:
        #     not_sort_list = self.list_name_table_column.listofElements(
        #         loc=f'td.ant-table-cell[data-column-key="{cell_name}"]')
        #     try:
        #         new_list = [not_sort_list.remove('')]
        #     except ValueError:
        #         continue
        #     else:
        #         print(new_list)
        #         if new_list == []:
        #             empty_column.append(cell_name)
        #     # else:
        #     #     allure.step(f'Sorted {cell_name} is not correct')
        #     column_name_list.remove(cell_name)
        # print(empty_column)"""



    def correct_sort(self):
        column_name_list = []
        error_list=[]
        for column_name in self.list_name_table_column.listofElements():
            if column_name.get_attribute('data-column-key') not in column_name_list:
                column_name_list.append(column_name.get_attribute('data-column-key'))
        reverse = False
        for i in range(1,3,1):
            tmp_list=list(column_name_list)
            for sorted_name in self.button_in.listofElements():
                # if self.button_sort.is_visible(): continue
                if reverse:
                    sorted_name.click()
                    sorted_name.click()
                else:
                    sorted_name.click()
                time.sleep(3)
                for cell_name in tmp_list:
                    not_sort_list = self.list_name_table_column.listofElements(loc=f'td.ant-table-cell[data-column-key="{cell_name}"]')
                    sort_list = sorted(not_sort_list, reverse=reverse)
                    if not_sort_list != sort_list:
                        error_list.append(f'Sorted {cell_name} is not correct')
                    tmp_list.remove(cell_name)
                    break
                if (tmp_list == []): break
            reverse = True
        assert error_list ==[], error_list

    def correct_filter(self, dict={}):
        start = time.time()
        self.button_filter_list.click()
        error_list = []
        for key in dict.keys():
            if key in ['clients_begin']:
                self.input_filter_version_date.click()
                self.input_filter_version_date.fill(dict.get(key), validate_value=False, enter=True)
                self.button_search.click()
                time.sleep(3)
                if len(self.list_name_table_column.listofElements(loc=f'td.ant-table-cell[data-column-key="{key}"]')) == 0:
                    error_list.append(f'No strings with this filter version_date = {dict.get(key)}')
                self.button_clear.click_by_text(keyword="Сбросить")

                self.input_filter_modified_date.click()
                self.input_filter_modified_date.fill(dict.get(key), validate_value=False, enter=True)
                self.button_search.click()
                if len(self.list_name_table_column.listofElements(
                        loc=f'td.ant-table-cell[data-column-key="{key}"]')) == 0:
                    error_list.append(f'No strings with this filter modified_date = {dict.get(key)}')
                self.button_clear.click_by_text(keyword="Сбросить")
                # not_sort_list = self.list_name_table_column.listofElements(loc=f'td.ant-table-cell[data-column-key="{key}"]')
                # for i in not_sort_list:
                #     if datetime.strptime(i, '%d.%m.%Y') > datetime.strptime(dict.get(key), '%d.%m.%Y') and key == 'clients_begin':
                #         error_list.append(f'Date begin {i} is more than date {dict.get(key)} in filter')
                #     if datetime.strptime(i, '%d.%m.%Y') < datetime.strptime(dict.get(key), '%d.%m.%Y') and key == 'clients_end':
                #         error_list.append(f'Date end {i} is less than date {dict.get(key)} in filter')
                # self.button_clear.click_by_text(keyword="Сбросить")
        #
            if key in ['clients_shortName', 'deals_shortName']:
                match key:
                    case 'clients_shortName':
                        self.input_filter_shortname.fill(dict.get(key), validate_value=False)
                    case 'deals_shortName':
                        self.input_filter_deal_shortname.fill(dict.get(key), validate_value=False)
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_name_table_column.listofElements(loc=f'td.ant-table-cell[data-column-key="{key}"]')
                for i in not_sort_list:
                    if dict.get(key).lower() not in i.lower():
                        error_list.append(f'The value {i} does not match the filter {dict.get(key)}')
                self.button_clear.click_by_text(keyword="Сбросить")

            if key in ['clients_inn', 'clients_ogrn', 'clients_kio', 'deals_inn_ogrn_kio']:
                self.input_filter_inn_ogrn_kio.fill(dict.get(key), validate_value=False)
                self.button_search.click()
                time.sleep(5)
                if key == 'deals_inn_ogrn_kio':
                    if len(self.list_name_table_column.listofElements()) == 0:
                        error_list.append(f'No strings with this filter {dict.get(key)}')
                else:
                    not_sort_list = self.list_name_table_column.listofElements(loc=f'td.ant-table-cell[data-column-key="{key}"]')
                    for i in not_sort_list:
                        if dict.get(key).lower() not in i.lower():
                            error_list.append(f'The value {i} does not match the filter {dict.get(key)}')
                self.button_clear.click_by_text(keyword="Сбросить")
        #
            if key in ['clients_bizSize']:
                self.input_filter_biz_size.fill(dict.get(key), validate_value=False,  enter=True)
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_name_table_column.listofElements(loc=f'td.ant-table-cell[data-column-key="{key}"]')
                for i in not_sort_list:
                    if dict.get(key).lower() not in i.lower():
                        error_list.append(f'The value {i} does not match the filter {dict.get(key)}')
                self.button_clear.click_by_text(keyword="Сбросить")
        #
            if key in ['clients_bizSegment']:
                self.input_filter_biz_segment.fill(dict.get(key), validate_value=False,  enter=True)
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_name_table_column.listofElements(loc=f'td.ant-table-cell[data-column-key="{key}"]')
                for i in not_sort_list:
                    if dict.get(key).lower() not in i.lower():
                        error_list.append(f'The value {i} does not match the filter {dict.get(key)}')
                self.button_clear.click_by_text(keyword="Сбросить")
        #
            if key in ['clients_countryName']:
                self.input_filter_country.fill(dict.get(key), validate_value=False,  enter=True)
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_name_table_column.listofElements(loc=f'td.ant-table-cell[data-column-key="{key}"]')
                for i in not_sort_list:
                    if dict.get(key).lower() not in i.lower():
                        error_list.append(f'The value {i} does not match the filter {dict.get(key)}')
                self.button_clear.click_by_text(keyword="Сбросить")
        #
            if key in ['clients_kpp', 'deals_kpp']:
                self.input_filter_kpp.fill(dict.get(key), validate_value=False)
                self.button_search.click()
                time.sleep(5)
                if key == 'deals_kpp':
                    if len(self.list_name_table_column.listofElements()) == 0:
                        error_list.append(f'No strings with this filter {dict.get(key)}')
                else:
                    not_sort_list = self.list_name_table_column.listofElements(loc=f'td.ant-table-cell[data-column-key="{key}"]')
                    for i in not_sort_list:
                        if dict.get(key).lower() not in i.lower():
                            error_list.append(f'The value {i} does not match the filter {dict.get(key)}')
                self.button_clear.click_by_text(keyword="Сбросить")
        #
            if key in ['checkbox']:
                self.input_filter_vzl.click()
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_name_table_column.listofElements()
                for i in not_sort_list:
                    i.click()
                    time.sleep(5)
                    if self.input_check_vzl.check_checkbox('ВЗЛ'):
                        break
                    else:
                        error_list.append(f'The checkbox "ВЗЛ" is not checked')
                        self.input_check_vzl.go_back()
                        time.sleep(2)
                        self.input_filter_vzl.click()
                        break

            if key in ['checkbox']:
                self.input_filter_byvzl.click()
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_name_table_column.listofElements()
                for i in not_sort_list:
                    i.click()
                    time.sleep(5)
                    if self.input_filter_byvzl.check_checkbox('Приравнен к ВЗЛ'):
                        break
                    else:
                        error_list.append(f'The checkbox "Приравнен к ВЗЛ" is not checked')
                        self.input_check_byvzl.go_back()
                        time.sleep(2)
                        self.input_filter_byvzl.click()
                        break

            if key in ['checkbox']:
                self.input_filter_ofshore.click()
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_name_table_column.listofElements()
                for i in not_sort_list:
                    i.click()
                    time.sleep(5)
                    if self.input_filter_ofshore.check_checkbox('Офшор'):
                        break
                    else:
                        error_list.append(f'The checkbox "Офшор" is not checked')
                        self.input_check_ofshore.go_back()
                        time.sleep(2)
                        self.input_filter_ofshore.click()
                        break

            if key == 'deals_dealTypeCD':
                self.input_filter_deal_type.click()
                self.input_filter_deal_type.fill(dict.get(key), validate_value=False)
                time.sleep(2)
                self.input_filter_deal_credit_transh.click(enter=True)
                self.button_search.click()
                time.sleep(2)
                not_sort_list = self.list_name_table_column.listofElements(
                    loc=f'td.ant-table-cell[data-column-key="{key}"]')
                for i in not_sort_list:
                    if dict.get(key).lower() not in i.lower():
                        error_list.append(f'The value {i} does not match the filter {dict.get(key)}')
                self.button_clear.click_by_text(keyword="Сбросить")
        #
            if key == 'deals_currencyCd':
                self.input_filter_currency.fill(dict.get(key), validate_value=False, enter=True)
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_name_table_column.listofElements(
                    loc=f'td.ant-table-cell[data-column-key="{key}"]')
                for i in not_sort_list:
                    if dict.get(key).lower() not in i.lower():
                        error_list.append(f'The value {i} does not match the filter {dict.get(key)}')
                self.button_clear.click_by_text(keyword="Сбросить")

            if key == 'deals_dealSumRur':
                sum_list = dict.get(key)
                self.input_filter_deal_sum_from.fill(sum_list[0], validate_value=False)
                self.input_filter_deal_sum_to.fill(sum_list[1], validate_value=False)
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_name_table_column.listofElements(
                    loc=f'td.ant-table-cell[data-column-key="{key}"]')
                for i in not_sort_list:
                    if i < sum_list[0] or i > sum_list[1]:
                        error_list.append(f'The value {i} does not match the filter sum from {sum_list[0]} and sum to {sum_list[1]}')
                self.button_clear.click_by_text(keyword="Сбросить")

            if key == 'deals_contractSi':
                date_list = dict.get(key)
                self.input_filter_deal_sign_date_from.click()
                self.input_filter_deal_sign_date_from.fill(str(date_list[0]), validate_value=False, enter=True)
                self.input_filter_deal_sign_date_to.click()
                self.input_filter_deal_sign_date_to.fill(str(date_list[1]), validate_value=False, enter=True)
                self.button_search.click()
                time.sleep(5)
                not_sort_list = self.list_name_table_column.listofElements(
                    loc=f'td.ant-table-cell[data-column-key="{key}"]')
                for i in not_sort_list:
                    cur_date = datetime.strptime(i, '%d.%m.%Y')
                    if cur_date < date_list[0] or cur_date > date_list[1]:
                        error_list.append(
                            f'The value {cur_date} does not match the filter date from {date_list[0]} and date to {date_list[1]}')
                self.button_clear.click_by_text(keyword="Сбросить")
                # for i in not_sort_list:
                #     i.click()
                #     if dict.get(key).lower() not in i.lower():
                #         error_list.append(f'The value {i} does not match the filter {dict.get(key)}')
                # self.button_clear.click()
            # self.button_search.click()
        # for keyword, cell_name in zip(keywords, cell_names):
        #     if cell_name == ['clients_begin','clients_end']:
        #         self.input_filter_version_date.fill(keyword, validate_value=True)
        #     if cell_name == 'clients_shortName':
        #         self.input_filter_shortname.fill(keyword, validate_value=True)
        #     if cell_name in ['clients_inn', 'clients_ogrn', 'clients_kio']:
        #         self.input_filter_inn_ogrn_kio.fill(keyword, validate_value=True)
        #     self.button_search.click()
        #     time.sleep(2)
        #     not_sort_list = self.list_name_table_column.listofElements(loc=f'td.ant-table-cell[data-column-key="{cell_name}"]')
        #     for i in not_sort_list:
        #         if keyword.lower() not in i.lower():
        #             error_list.append(f'The value {i} does not match the filter {keyword}')
        #         # assert keyword.lower() in i.lower(), f'The value {i} does not match the filter {keyword}'
        end = time.time() - start
        print(end)
        print(error_list)
        assert len(error_list) == 0, error_list