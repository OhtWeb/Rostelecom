Автотесты для LK/RT — Руководство

Кратко: проект реализует PageObject-паттерн для веб‑приложения Ростелекома. Тесты написаны на pytest + Selenium, конфигурация через .env. Некоторые сценарии (CAPTCHA, OTP) частично автоматизированы — позитивные проходы требуют ручного ввода, негативные — автоматизированы.

——————————

Содержимое репозитория (кратко)

• pageobject/

• pages/ — PageObject страницы:

• base_page.py — базовый класс со вспом. методами (open, find_element, click_element, enter_text, is_element_present, get_error_text и т.д.)

• auth_page.py — методы для авторизации (login_by_password, request_temporary_code, enter_temp_code, is_temp_code_invalid и т.п.)

• password_recovery_page.py — методы для восстановления пароля

• registration_page.py — методы для регистрации

• locators.py — все локаторы (AuthLocators и т.п.)

• settings.py — конфигурация (подтягивается из .env, таймауты, тестовые данные)

• conftest.py — фикстуры pytest (browser, setup/teardown)


• tests/ — тесты:

• test_auth_page.py

• test_password_recovery_page.py

• test_registration_page.py


• .env — приватные данные (в репозитории используются плэйсхолдеры, изменить перед началом работы)

• pytest.ini — конфигурация pytest (уровень логирования, опции по умолчанию)

• requirements.txt — зависимости проекта

• .gitignore — игнорируемые файлы (включая .env, драйвера и т.п.)


——————————

Установка (локально)

1. Устанавливить зависимости:

- Минимальный набор:
  pip install -r requirements.txt
 (Состав requirements.txt:

  - pytest
  - selenium
  - python-dotenv
  - webdriver-manager)

2. Заполнить .env

3. Запуск браузера (conftest / webdriver-manager)

Пример фикстуры в conftest.py:

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
  def browser():
      """Фикстура для создания и закрытия браузера перед и после теста."""
      print("\nЗапуск браузера для теста...")

      # Настройка опций браузера (опционально)
      options = webdriver.ChromeOptions()
      # options.add_argument("--headless") # Раскомментируйте для запуска без графического окна

      # Инициализация драйвера
      driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
      driver.implicitly_wait(5)  # Неявное ожидание для подстраховки

      # Передаем драйвер в тест
      yield driver

      # Код после yield выполнится ВСЕГДА по окончании теста
      print("\nЗакрытие браузера...")
      driver.quit()

——————————

Как запускать тесты

• Запустить все тесты:

  python -m pytest
  
  
• Запустить конкретный файл:

  python -m pytest pageobject/tests/test_auth_page.py
  
  
• Запустить один тест:

  python -m pytest pageobject/tests/test_auth_page.py::test_auth_with_invalid_password -v -s
  
——————————

Описания тестов (кратко)
-----------
test_auth_page.py

1. Проверка входа с верными данными пользователя  

2. Проверка входа с неверными данными пользователя (логин и пароль)  

3. Проверка входа при отсутствии логина  

4. Проверка входа при отсутствии пароля  

5. Проверка входа при неверном регистре  

6. Проверка на SQL-инъекцию (негативные данные в полях)  

7. Проверка на XSS-инъекцию (вставка скрипта в поля — проверка экранирования)  

8. Проверка авторизации по неверному временному коду (негативный сценарий)

Примечание: позитивный сценарий авторизации через OTP/временный код автоматизировать сложно из‑за ограничений с доставкой кода.

-----------
test_password_recovery_page.py

1. Проверка работоспособности кнопки восстановления пароля (открытие формы)  

2. Проверка ввода верной капчи — ДЕМО логики (выполняется как демонстрация; обычно требует ручного ввода)  

3. Проверка ввода неверной капчи (автоматизировано — негатив)  

4. Попытка восстановления без ввода капчи (валидация)  

5. Проверка отмены восстановления (кнопка Назад)

-----------
test_registration_page.py

1. Проверка имени несоответствующей длины (boundary values)  

2. Проверка имени не на кириллице (если требование — кириллица)  

3. Проверка слишком короткого пароля (минимальная длина)  

4. Проверка пароля без заглавных букв (требования сложности)  

5. Проверка пароля без строчных букв  

6. Проверка кнопки "Показать пароль" (UI behaviour)  

7. Проверка ввода несуществующего региона (валидация/фоллбек)  

8. Проверка поля email/телефон в неверном формате (validation)

