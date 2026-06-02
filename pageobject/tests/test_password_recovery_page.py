import pytest
from pageobject.pages.auth_page import AuthPage
from pageobject.pages.password_recovery_page import PasswordRecoveryPage
from pageobject.pages.settings import Settings

# 1. Проверка работоспособности кнопки восстановления пароля
def test_recovery_button_available(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    recovery_page = PasswordRecoveryPage(browser)
    print("\n--- Запуск теста: test_recovery_button_available ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    recovery_page.open_recovery_form()
    is_captcha_visible = recovery_page.is_captcha_visible()
    assert is_captcha_visible, "Переход на страницу восстановления пароля не выполнен!"
    if is_captcha_visible:  # Только если тест прошел успешно
        print("Успешный переход на страницу восстановления пароля!")
    print("--- Тест test_recovery_button_available завершен ---")

# 2. Проверка ввода верной капчи
@pytest.mark.skip(reason='''Автоматизация ввода реальной капчи невозможна без интеграции 
со сторонними сервисами распознавания''')
def test_correct_captcha(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    recovery_page = PasswordRecoveryPage(browser)
    print("\n--- Запуск теста: test_correct_captcha ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    recovery_page.open_recovery_form()

    '''ПРИМЕЧАНИЕ К АВТОМАТИЗАЦИИ:
    Данный тест предназначен исключительно для демонстрации логики тест-кейса. 
    Полноценная автоматизация ввода валидной капчи в промышленной среде невозможна, так как:
    1. Это противоречит базовому назначению CAPTCHA (защите от автоматизированных скриптов).
    2. Интеграция сторонних сервисов распознавания (OCR / ИИ) выходит за рамки текущих задач.'''

    recovery_page.enter_captcha_and_submit(Settings.LOGIN,'MOCK_VALID_CAPTCHA')
    is_captcha_correct = recovery_page.is_captcha_correct()
    assert is_captcha_correct, "Система не обработала ввод верной капчи или не перенаправила пользователя!"
    if is_captcha_correct:
        print("Проверка капчи успешна, осуществлен переход на страницу ввода персонального кода восстановления")
    print("--- Тест test_correct_captcha завершен ---")

# 3. Проверка ввода неверной капчи
def test_wrong_captcha(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    recovery_page = PasswordRecoveryPage(browser)
    print("\n--- Запуск теста: test_wrong_captcha ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    recovery_page.open_recovery_form()
    recovery_page.enter_captcha_and_submit(Settings.LOGIN, Settings.DUMMY_CAPTCHA)
    is_captcha_wrong = recovery_page.get_captcha_error_text()
    assert is_captcha_wrong, "Сообщение об ошибке ввода капчи не появилось на странице!"
    if is_captcha_wrong:
        print("Ввод неверной капчи успешно обработан, сообщение об ошибке получено")
    print("--- Тест test_wrong_captcha завершен ---")

# 4. Проверка попытки входа без ввода капчи
def test_missing_captcha_input(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    recovery_page = PasswordRecoveryPage(browser)
    print("\n--- Запуск теста: test_missing_captcha_input ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    recovery_page.open_recovery_form()

    # Отправляем пустую строку вместо капчи
    recovery_page.enter_captcha_and_submit(Settings.LOGIN, '')
    is_validation_triggered = recovery_page.get_captcha_error_text()

    assert is_validation_triggered, "Система не вывела предупреждение о необходимости заполнить поле капчи!"
    if is_validation_triggered:
        print("Система заблокировала отправку формы с пустой капчей")
    print("--- Тест test_missing_captcha_input завершен ---")

# 5. Проверка отмены восстановления пароля
def test_cancel_recovery(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    recovery_page = PasswordRecoveryPage(browser)
    print("\n--- Запуск теста: test_cancel_recovery ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    recovery_page.open_recovery_form()
    recovery_page.cancel_recovery_at_captcha_stage()

    is_recovery_cancelled = recovery_page.return_to_auth_page()
    assert is_recovery_cancelled, "Система не осуществила возврат на страницу авторизации!"
    if is_recovery_cancelled:
        print("Система успешно осуществила возврат на страницу авторизации!")
    print("--- Тест test_cancel_recovery завершен ---")