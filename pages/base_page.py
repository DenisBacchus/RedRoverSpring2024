from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from locators.login_locators import LoginLocators
from src.user_data import UserData


class BasePage:
    timeout = 10
    locators = LoginLocators()
    user = UserData()

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def login(self):
        self.element_is_visible(self.locators.USER_NAME).send_keys(self.user.standard_user)
        self.element_is_visible(self.locators.PASSWORD).send_keys(self.user.password)
        self.element_is_clickable(self.locators.LOGIN).click()

    def open(self):
        self.driver.get(self.url)

    def get_text(self, locator):
        return self.element_is_visible(locator).text

    def get_length(self, locator):
        return len(self.elements_are_visible(locator))

    def click_to_element(self, locator):
        self.element_is_clickable(locator).click()

    def element_is_clickable(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_not_present(self, locator, timeout=timeout):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_displayed(self, element):
        return element.is_displayed()

    def select_by_value(self, locator, value):
        select_element = self.driver.find_element(*locator)
        select = Select(select_element)
        select.select_by_value(value)

