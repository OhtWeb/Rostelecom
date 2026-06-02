from .base_page import BasePage
from .locators import AuthLocators


class RegistrationPage(BasePage):
    def __init__(self, browser, url="https://rt.ru"):
        super().__init__(browser, url)

    def fill_name(self, name):
        self.enter_text(AuthLocators.AUTH_FIRST_NAME, name)
    def fill_surname(self, surname):
        self.enter_text(AuthLocators.AUTH_LAST_NAME, surname)
    def fill_email(self, email):
        self.enter_text(AuthLocators.AUTH_EMAIL, email)
    def fill_password(self, password):
        self.enter_text(AuthLocators.AUTH_PASS, password)
    def confirm_password(self, password):
        self.enter_text(AuthLocators.AUTH_PASS_CONFIRM, password)
    def fill_region(self, region):
        elements = self.browser.find_elements(*AuthLocators.REGION)
        elements[2].send_keys(region)
    def submit(self):
        self.click_element(AuthLocators.BTN_REGISTER)
    def is_form_incorrect(self):
        return self.is_element_present(AuthLocators.REG_FORM_ERROR, timeout=5)
    def click_anywhere(self):
        self.click_element(AuthLocators.BTN_ANYWHERE)
    def click_show_password_btn(self):
        self.click_element(AuthLocators.BTN_SHOW_PASS)
    def get_password_field_type(self):
        element = self.find_element(AuthLocators.AUTH_PASS)
        return element.get_attribute("type")
    def get_region_error_message(self):
        return self.is_element_present(AuthLocators.REGION_ERROR, timeout=5)
