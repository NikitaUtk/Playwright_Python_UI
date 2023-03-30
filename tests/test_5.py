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
        role_page.navbar.visit_clients_page()
        time.sleep(2)
        form_date = date.today() - timedelta(days=10)
        cur_date = form_date.strftime('%d.%m.%Y')
        role_page.navbar.search_modal.correct_filter(dict={'clients_begin':str(cur_date), 'clients_shortName': 'ВТБ', 'clients_inn':'0274953485', 'clients_ogrn': '1190280085995',
                                                           'clients_kio':'22222', 'clients_bizSize':'Крупный бизнес', 'clients_bizSegment':'Инвестиционные проекты', 'clients_countryName':'RUS', 'clients_kpp':'0', 'checkbox':''})