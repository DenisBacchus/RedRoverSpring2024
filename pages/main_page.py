import random
import time

from selenium.webdriver.support.select import Select

from locators.login_locators import LoginLocators
from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    main_locators = MainLocators()
    login_locators = LoginLocators()

    def logout(self):
        self.click_to_element(self.main_locators.BURGER_MENU)
        self.click_to_element(self.main_locators.LOGOUT_BTN)

    def check_element_is_displayed(self):
        login_form = self.element_is_visible(self.login_locators.LOGIN_FORM)
        return self.element_is_displayed(login_form)

    def select(self, value):
        locator = self.main_locators.SELECT
        self.select_by_value(locator=locator, value=value)

    def get_price(self):
        lst = self.elements_are_visible(self.main_locators.PRICE_VALUE)
        lst_price = [i.text for i in lst]
        return lst_price

    def check_filter(self, value):
        self.select(value)
        lst = self.get_price()
        return lst

    def add_to_cart(self):
        self.click_to_element(self.main_locators.SAUCE_LABS_BACKPACK)
        value = self.element_is_visible(self.main_locators.COUNT_ITEMS)
        return value

    def remove_from_cart(self):
        self.click_to_element(self.main_locators.REMOVE_SAUCE_LABS_BACKPACK)

    def check_elem_is_not_present(self):
        return self.element_is_not_present(self.main_locators.COUNT_ITEMS)