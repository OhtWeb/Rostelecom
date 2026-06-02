from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import AuthLocators

class PasswordRecoveryPage(BasePage):
    def __init__(self, browser, url="https://rt.ru"):
        # Инициализируем родительский класс со специальным URL
        super().__init__(browser, url)

    def open_recovery_form(self):
        # Нажатие на кнопку "Забыли пароль" на главной странице авторизации
        self.click_element(AuthLocators.AUTH_FORGOT_PASS_BTN)
        return self.is_element_present(AuthLocators.AUTH_CAPTCHA, timeout=5)

    def enter_captcha_and_submit(self, login, captcha_text):
        # Ввод символов с картинки и запуск восстановления.
        # Вообще, Автоматизация ввода капчи через Selenium напрямую невозможна.
        self.enter_text(AuthLocators.AUTH_LOGIN, login)
        self.enter_text(AuthLocators.AUTH_CAPTCHA, captcha_text)
        self.click_element(AuthLocators.AUTH_RESET_PASS_BTN)

    def cancel_recovery_at_captcha_stage(self):
        # Отмена восстановления и возврат на страницу авторизации
        self.click_element(AuthLocators.AUTH_CANCEL_RESET_PASS_BTN)

    def return_to_auth_page(self):
        return self.is_element_present(AuthLocators.LOGIN_BTN)

    def is_captcha_visible(self):
        # Проверка, появилась ли капча на экране
        return self.is_element_present(AuthLocators.AUTH_CAPTCHA, timeout=5)

    def get_captcha_error_text(self):
        # Получаем текст ошибки под полем капчи
        return self.is_element_present(AuthLocators.AUTH_CAPTCHA_ERROR)

    def is_captcha_correct(self):
        return self.is_element_present(AuthLocators.AUTH_RESET_RECOVERY, timeout=5)

    def get_captcha_image_source(self):
        captcha_element = self.find_element(AuthLocators.CAPTCHA_IMAGE, timeout=10)
        return captcha_element.get_attribute("src")

    def wait_for_captcha_src_to_change(self, old_src, timeout=10):
        #Ожидаем, пока атрибут src картинки изменится со старого значения на любое другое."""
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.text_to_be_present_in_element_attribute(AuthLocators.CAPTCHA_IMAGE, "src", old_src)
            )
            return True
        except:
            return False

    def refresh_captcha_image(self):
        self.click_element(AuthLocators.CAPTCHA_RELOAD_BTN)