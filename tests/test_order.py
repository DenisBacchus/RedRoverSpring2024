import time

import pytest

from pages.order_page import OrderPage
from src.order_data import OrderData
from src.urls import Urls


class TestOrder:
    url = Urls()
    data = OrderData()

    def test_order_with_valid_credential(self, driver):
        page = OrderPage(driver, self.url.base_url)
        page.open()
        page.login()
        expected_text = page.order_with_valid_credential(self.data.user_data_with_valid_credential)
        assert self.data.successful_message == expected_text, \
            f"Unexpected text, expected text: {expected_text}, actual text: {self.data.successful_message}"

    @pytest.mark.parametrize("lst_data", data.user_data)
    def test_order_with_wrong_credential(self, driver, lst_data):
        page = OrderPage(driver, self.url.base_url)
        page.open()
        page.login()
        expected_text = page.order_with_wrong_credential(lst_data)
        assert lst_data[3] == expected_text, \
            f"Unexpected text, expected text: {expected_text}, actual text: {lst_data[3]}"
