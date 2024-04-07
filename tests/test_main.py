import time

import pytest

from functions.functions import sort_list
from pages.main_page import MainPage
from src.main_data import MainData
from src.urls import Urls


class TestMainPage:
    url = Urls()
    main_data = MainData()

    def test_logout(self, driver):
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.logout()
        value = page.check_element_is_displayed()
        assert driver.current_url == self.url.base_url and value is True, "Форма логинки не видна"

    @pytest.mark.parametrize("value", main_data.price)
    def test_select(self, driver, value):
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        lst = page.check_filter(value[0])
        assert lst == sort_list(lst, value[1]), value[2]

    def test_add_item_to_cart(self, driver):
        expected_value = "1"
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        value = page.add_to_cart()
        assert value.text == expected_value, f"Количество добавленных товаров не соответствует {expected_value}"

    def test_remove_item_from_cart(self, driver):
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.add_to_cart()
        page.remove_from_cart()
        value = page.check_elem_is_not_present()
        assert value is True, "Элемент присутствует в DOM-дереве"
