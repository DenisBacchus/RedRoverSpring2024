

class OrderLocators:
    FIRST_NAME = ("css selector", "input[data-test='firstName']")
    LAST_NAME = ("css selector", "input[data-test='lastName']")
    ZIP_CODE = ("css selector", "input[data-test='postalCode']")
    CONTINUE_BTN = ("css selector", "input[id='continue']")
    FINISH_BTN = ("css selector", "button[id='finish']")
    SUCCESSFUL_ORDER = ("css selector", "h2[data-test='complete-header']")
    ERROR_MESSAGE = ("css selector", "h3[data-test='error']")
