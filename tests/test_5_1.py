import pytest

from pages.home_page import HomePage
from pages.role_page import RolesPage
from settings import *
import playwright
from playwright.sync_api import Page
import time
from datetime import date, timedelta, datetime

class TestCase:
    @pytest.mark.parametrize('keyword', ['Эксперт'])
    def test2(
        self,
        keyword: str,
        home_page: HomePage,
        role_page: RolesPage
    ):
        home_page.visit(API_URL+"api/Users")
        home_page.visit(WEB_URL)
        home_page.navbar.open_roleList()
        home_page.navbar.visit_role_page(keyword)

        role_page.role_present(role=keyword)
        role_page.navbar.visit_deals_page()
        time.sleep(3)
        date_from = date(2022, 8, 10)
        date_to = date(2022, 12, 10)
        form_date = date.today() - timedelta(days=10)
        cur_date = form_date.strftime('%d.%m.%Y')
        role_page.navbar.search_modal.correct_filter(
            dict={'modified_date':str(cur_date), 'deals_dealTypeCD': 'Кредитная сделка. Транш', 'deals_currencyCd': 'RUR', 'deals_dealSumRur':['10000000.00', '20000000.00'], 'deals_contractSignDate':[date_from.strftime('%d.%m.%Y'), date_to.strftime('%d.%m.%Y')],
                  'deals_shortName':'ВТБ', 'deals_inn_ogrn_kio':'11', 'deals_kpp':'0', 'abs_code':'114738465|#%191', 'deals_contractTerm':['1000', '5000'], 'deals_contractNum':'11',
                  'deals_rate':{'deals_rateTypeCd':['Фиксированная', 'Плавающая'],'deals_rateAmount':['5','15'], 'deals_rateFix':['1','1'], 'deals_rateIndCD':'Ключевая'}})
