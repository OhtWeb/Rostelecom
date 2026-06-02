from selenium.webdriver.common.by import By

class AuthLocators:
    #Блок локаторов выбора типа авторизации lk.rt.ru: логин/пароль или временный код
    AUTH_ADDRESS = (By.ID, "address")
    AUTH_GET_CODE = (By.ID, "otp_get_code")
    AUTH_ENTER_WITH_PASS = (By.ID, "standard_auth_btn")

    #Блок локаторов форм ввода lk.rt.ru, lk.smarthome.rt.ru
    AUTH_LOGIN = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_PASS_CONFIRM = (By.ID, "password_confirm")
    LOGIN_BTN = (By.ID, "kc-login")
    LOGOUT_BTN = (By.CLASS_NAME, "profile-logout")
    CHECKPOINT_ELEMENT = (By.ID, "root")
    CHECKPOINT_ERROR = (By.ID, "form-error-message")
    LOGIN_MISSING = (By.ID, "username-meta")
    SECURITY_WARNING = (By.XPATH, "//*[contains(text(), 'из соображений безопасности')]")

    #Блок локаторов сценария восстановления пароля
    AUTH_FORGOT_PASS_BTN = (By.ID, "forgot_password")
    AUTH_CAPTCHA = (By.ID, "captcha")
    AUTH_RESET_PASS_BTN = (By.ID, "reset")
    AUTH_CANCEL_RESET_PASS_BTN = (By.ID, "reset-back")
    AUTH_CAPTCHA_ERROR = (By.ID, "form-error-message")
    AUTH_RESET_RECOVERY = (By.ID, "reset-cancel")
    AUTH_CODE_INPUT = (By.ID, "rt-code-input")
    CAPTCHA_IMAGE = (By.PARTIAL_LINK_TEXT, "https://webapi.passport.rt.ru/captcha/getcaptcha")
    CAPTCHA_RELOAD_BTN = (By.CLASS_NAME, "rt-captcha__reload")

    #Блок локаторов для временного кода lk.rt.ru, lk.smarthome.rt.ru
    AUTH_TEMP_CODE_WINDOW_1 = (By.ID, "rt-code-0")
    AUTH_TEMP_CODE_WINDOW_2 = (By.ID, "rt-code-1")
    AUTH_TEMP_CODE_WINDOW_3 = (By.ID, "rt-code-2")
    AUTH_TEMP_CODE_WINDOW_4 = (By.ID, "rt-code-3")
    AUTH_TEMP_CODE_WINDOW_5 = (By.ID, "rt-code-4")
    AUTH_TEMP_CODE_WINDOW_6 = (By.ID, "rt-code-5")

    #Блок локаторов для страницы my.rt.ru
    AUTH_BACK_TO_PROFILE_BTN = (By.CLASS_NAME, "reset-form__reset-btn")
    AUTH_ANOTHER_LOGIN = (By.CLASS_NAME, "rt-link--orange")

    # Универсальный локатор для вывода ошибок на формах
    FORM_ERROR_MSG = (By.ID, "form-error-message")

    #Блок локаторов для регистрации
    AUTH_LAST_NAME = (By.NAME, "lastName")
    AUTH_FIRST_NAME = (By.NAME, "firstName")
    AUTH_PATRONYMIC = (By.NAME, "patronymic")
    AUTH_EMAIL = (By.NAME, "address")
    CONFIRM_CODE_INPUT = (By.ID, "code_input")
    BTN_FORWARD = (By.PARTIAL_LINK_TEXT, "Далее")
    BTN_BACK = (By.PARTIAL_LINK_TEXT, "Назад")
    REGION = (By.CSS_SELECTOR, ".rt-input__input--rounded.rt-input__input--orange")
    BTN_FORM_REGISTER = (By.ID, 'kc-register')
    BTN_REGISTER = (By.NAME, "register")
    REG_FORM_ERROR = (
    By.CSS_SELECTOR,
    ".rt-input-container__meta.rt-input-container__meta--error",
)
    BTN_ANYWHERE = (By.ID, "page-right")
    BTN_SHOW_PASS = (By.CSS_SELECTOR, ".rt-eye-icon.rt-input__eye")
    REGION_ERROR = (By.CSS_SELECTOR, ".rt-select__list-no-found")

    #Кнопка выхода из аккаунта находится на отдельной стринце https://lk.smarthome.rt.ru/profile?section=my_account
    BTN_LOGOUT = (By.PARTIAL_LINK_TEXT, "Выйти")

    #Блок локаторов для key.rt.ru
    BTN_ENTER = (By.CLASS_NAME, "go_kab")
    #кнопка некликабельна в штатном режиме. Впрочем, на странице вообще ВСЁ некликабельно
