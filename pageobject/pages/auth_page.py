from .base_page import BasePage
from .locators import AuthLocators

class AuthPage(BasePage):
    def __init__(self, browser, url="https://rt.ru"):
        super().__init__(browser, url)

    def choose_auth_by_password(self):
        # Переключение на авторизацию по паролю
        self.click_element(AuthLocators.AUTH_ENTER_WITH_PASS)

    def login_with_password(self, login, password):
        # Шаги для полной авторизации по логину и паролю
        self.enter_text(AuthLocators.AUTH_LOGIN, login)
        self.enter_text(AuthLocators.AUTH_PASS, password)
        self.click_element(AuthLocators.LOGIN_BTN)

    def request_temporary_code(self, address):
        # Получение временного кода на адрес/телефон
        self.enter_text(AuthLocators.AUTH_ADDRESS, address)
        self.click_element(AuthLocators.AUTH_GET_CODE)

    def is_user_logged_in(self):
        # Проверка, что авторизация прошла успешно
        return self.is_element_present(AuthLocators.CHECKPOINT_ELEMENT)

    def is_data_entry_wrong(self):
        return self.is_element_present(AuthLocators.CHECKPOINT_ERROR)

    def is_login_missing(self):
        return self.is_element_present(AuthLocators.LOGIN_MISSING)

    def is_security_warning(self):
        return self.is_element_present(AuthLocators.SECURITY_WARNING)

    def open_registration_form(self):
        self.click_element(AuthLocators.BTN_FORM_REGISTER)