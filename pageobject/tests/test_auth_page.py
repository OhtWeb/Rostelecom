from pageobject.pages.settings import Settings
from pageobject.pages.auth_page import AuthPage

# 1. Проверка входа с верными данными пользователя
def test_auth_with_valid_password(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)  # Берем URL из настроек
    print("\n--- Запуск теста: test_auth_with_valid_password ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    print(f"Попытка авторизации с Вашим логином")

    # Используем данные из .env
    auth_page.login_with_password(Settings.LOGIN, Settings.PASSWORD)

    is_logged_in = auth_page.is_user_logged_in()
    assert is_logged_in, "Авторизация не удалась с валидными данными!"
    if is_logged_in:  # Только если тест прошел успешно
        print("Успешная авторизация с валидными данными!")
    print("--- Тест test_auth_with_valid_password завершен ---")

# 2. Проверка входа с неверными данными пользователя (логин И пароль)
def test_auth_with_invalid_data(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    print("\n--- Запуск теста: test_auth_with_invalid_password ---")
    auth_page.open()
    auth_page.choose_auth_by_password()

    invalid_login = Settings.INVALID_LOGIN
    invalid_password = Settings.INVALID_PASSWORD
    print(f"Попытка авторизации с неверными логином/паролем: {invalid_login}/{invalid_password}")
    auth_page.login_with_password(invalid_login, invalid_password)

    is_wrong_data = auth_page.is_data_entry_wrong()
    assert is_wrong_data, "Сообщение об ошибке при неверных данных не появилось!"
    if is_wrong_data:  # Только если тест прошел успешно
        print("Успешная проверка: система выдала ошибку при неверных данных!")
    print("--- Тест test_auth_with_invalid_password завершен ---")

# 3. Проверка входа с отсутствующим логином
def test_auth_with_missing_login(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    print("\n--- Запуск теста: test_auth_with_missing_login ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    print(f"Попытка авторизации с отсутствующим логином и верным паролем")
    invalid_login = ''
    auth_page.login_with_password(invalid_login, Settings.PASSWORD)

    is_login_missing = auth_page.is_login_missing()
    assert is_login_missing, "Сообщение об ошибке при отсутствующих данных не появилось!"
    if is_login_missing:  # Если тест прошел успешно
        print("Успешная проверка: система выдала ошибку при неполных данных!")
    print("--- Тест test_auth_with_invalid_password завершен ---")

# 4. Проверка входа с отсутствующим паролем
def test_auth_with_missing_password(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    print("\n--- Запуск теста: test_auth_with_missing_password ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    print(f"Попытка авторизации с верным логином и отсутствующим паролем")
    invalid_password = ''
    auth_page.login_with_password(Settings.LOGIN, invalid_password)

    is_wrong_data = auth_page.is_data_entry_wrong()
    assert is_wrong_data, "Сообщение об ошибке при неполных данных не появилось!"
    if is_wrong_data:  # Если тест прошел успешно
        print("Успешная проверка: система выдала ошибку при неполных данных!")
    print("--- Тест test_auth_with_invalid_password завершен ---")

# 5. Проверка входа с неверным регистром
def test_auth_password_case_sensitivity(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    print("\n--- Запуск теста: test_auth_password_case_sensitivity ---")
    auth_page.open()
    auth_page.choose_auth_by_password()

    # Инвертируем регистр валидного пароля
    wrong_case_password = Settings.PASSWORD.swapcase()
    print(f"Попытка авторизации с измененным регистром пароля")

    auth_page.login_with_password(Settings.LOGIN, wrong_case_password)

    is_wrong_data = auth_page.is_data_entry_wrong()
    assert is_wrong_data, "Система пустила пользователя с паролем в неверном регистре!"
    if is_wrong_data:
        print("Успешная проверка: система чувствительна к регистру пароля!")
    print("--- Тест test_auth_password_case_sensitivity завершен ---")

# 6. Проверка системы на SQL-инъекцию
def test_auth_sql_injection_in_login(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    print("\n--- Запуск теста: test_auth_sql_injection_in_login ---")
    auth_page.open()
    auth_page.choose_auth_by_password()

    # Пытаемся обойти проверку условия WHERE
    sql_login = "' OR '1'='1"
    print(f"Попытка авторизации с SQL-инъекцией в логине: {sql_login}")

    auth_page.login_with_password(sql_login, Settings.PASSWORD)

    # Проверяем, что база данных/бэкенд не упали (500 ошибка) и фронтенд показал ошибку данных
    is_security_warning = auth_page.is_security_warning()
    assert is_security_warning, "Система уязвима к SQL-инъекции или не вывела ошибку валидации!"
    if is_security_warning:
        print("Успешная проверка: система безопасно обработала SQL-инъекцию!")
    print("--- Тест test_auth_sql_injection_in_login завершен ---")

# 7. Проверка системы на XSS-инъекцию
def test_auth_xss_injection_in_login(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    print("\n--- Запуск теста: test_auth_xss_injection_in_login ---")
    auth_page.open()
    auth_page.choose_auth_by_password()

    # XSS-пейлоад. Если система уязвима, она выполнит скрипт и вызовет модальное окно alert
    xss_login = "<script>alert('XSS')</script>"
    print(f"Попытка авторизации с XSS-инъекцией в логине: {xss_login}")

    auth_page.login_with_password(xss_login, Settings.PASSWORD)

    # Проверяем, что браузер не открыл непредвиденное модальное окно (alert) от скрипта
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        alert.dismiss()
        assert False, f"Внимание! Скрипт XSS выполнился! Текст алерта: {alert_text}"
    except:
        print("Браузерный alert не появился — скрипт не выполнился (безопасно)")

    # Проверяем, что база данных/бэкенд не упали (500 ошибка) и фронтенд показал ошибку данных
    is_security_warning = auth_page.is_security_warning()
    assert is_security_warning, "Ошибка валидации при XSS-вводе не появилась!"

    print("--- Тест test_auth_xss_injection_in_login завершен ---")

#8. Проверка авторизации по неверному временному коду

def test_auth_with_invalid_code(browser):
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    print("\n--- Запуск теста: test_auth_with_invalid_code ---")
    auth_page.open()
    auth_page.fill_login_form(Settings.LOGIN)
    auth_page.request_temporary_code()
    invalid_code = "012345"
    print(f"Переходим на страницу ввода временного кода")
    auth_page.enter_temp_code(invalid_code)

    is_invalid_code = auth_page.is_temp_code_invalid()
    assert is_invalid_code, "Сообщение об ошибке при неверных данных не появилось!"
    if is_invalid_code:
        print("Успешная проверка: система выдала ошибку при неверном коде!")
    print("--- Тест test_auth_with_valid_password завершен ---")