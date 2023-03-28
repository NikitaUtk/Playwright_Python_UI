import pytest

from pages.home_page import HomePage
from pages.role_page import RolesPage
from settings import *
import playwright
from playwright.sync_api import Page
import time
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
        time.sleep(5)
        role_page.navbar.search_modal.find_empty_column()

