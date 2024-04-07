import random


class MainLocators:
    TITLE = ("css selector", "span[data-test='title']")
    CARDS = ("css selector", "div[data-test='inventory-item']")
    SAUCE_LABS_BACKPACK = ("css selector", "button[data-test='add-to-cart-sauce-labs-backpack']")
    REMOVE_SAUCE_LABS_BACKPACK = ("css selector", "button[data-test='remove-sauce-labs-backpack']")
    CART_BTN = ("css selector", "a[data-test='shopping-cart-link']")
    BURGER_MENU = ("css selector", "div[class='bm-burger-button']")
    LOGOUT_BTN = ("css selector", "a[data-test='logout-sidebar-link']")
    SELECT = ("xpath", "//select[@data-test='product-sort-container']")
    PRICE_VALUE = ("css selector", "div[data-test='inventory-item-price']")
    COUNT_ITEMS = ("css selector", "span[data-test='shopping-cart-badge']")
