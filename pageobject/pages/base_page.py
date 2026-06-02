from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .settings import Settings
from .locators import AuthLocators

class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.timeout = Settings.DEFAULT_TIMEOUT

    def open(self):
        self.browser.get(self.url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_element_present(self, locator, timeout=10):
        try:
            self.find_element(locator, timeout)
        except TimeoutException:
            return False
        return True

    def get_error_text(self, timeout=10):
        try:
            element = self.find_element(AuthLocators.FORM_ERROR_MSG, timeout)
            return element.text
        except TimeoutException:
            return None