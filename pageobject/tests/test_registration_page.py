import pytest
from pageobject.pages.registration_page import RegistrationPage
from pageobject.pages.auth_page import AuthPage
from pageobject.pages.settings import Settings
import random
import string

# 1. Проверка имени несоответствующей длины
def test_registration_wrong_name_length(browser):
    # Имя генерируем случайным образом
    characters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    length = random.choice([random.randint(1, 1), random.randint(30, 40)])
    name = "".join(random.choice(characters) for _ in range(length))
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    registration_page = RegistrationPage(browser)
    print("\n--- Запуск теста: test_registration_wrong_name_length ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    auth_page.open_registration_form()
    registration_page.fill_name(name)
    registration_page.click_anywhere()

    is_form_incorrect = registration_page.is_form_incorrect()
    assert is_form_incorrect, "Форма ввода имени позволяет ввод имени длиной менее двух/более 30 символов!"
    if is_form_incorrect:
        print("Ограничения по длине имени работают корректно!")
    print("--- Тест test_registration_wrong_name_length завершен ---")

# 2. Проверка некириллического имени
def test_registration_wrong_name_non_cyrillic(browser):
    # Имя генерируем случайным образом
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(){}[]"
    length = random.choice([random.randint(2, 30)])
    name = "".join(random.choice(characters) for _ in range(length))
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    registration_page = RegistrationPage(browser)
    print("\n--- Запуск теста: test_registration_wrong_name_non_cyrillic ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    auth_page.open_registration_form()
    registration_page.fill_name(name)
    registration_page.click_anywhere()

    is_form_incorrect = registration_page.is_form_incorrect()
    assert is_form_incorrect, "Форма ввода имени позволяет ввод имени из некириллических символов!"
    if is_form_incorrect:
        print("Ограничения по типу символов работают корректно!")
    print("--- Тест test_registration_wrong_name_non_cyrillic завершен ---")

# 3. Проверка слишком короткого пароля
def test_registration_wrong_password_to_short(browser):
    characters = string.ascii_letters + string.digits
    length = random.choice([random.randint(1, 7)])
    password = "".join(random.choice(characters) for _ in range(length))
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    registration_page = RegistrationPage(browser)
    print("\n--- Запуск теста: registration_wrong_password_to_short ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    auth_page.open_registration_form()
    registration_page.fill_password(password)
    registration_page.click_anywhere()

    is_form_incorrect = registration_page.is_form_incorrect()
    assert is_form_incorrect, "Форма ввода пароля позволяет ввод пароля длиной менее 8 символов!"
    if is_form_incorrect:
        print("Ограничения по длине пароля работают корректно!")
    print("--- Тест registration_wrong_password_to_short завершен ---")

# 4. Проверка пароля без прописных букв
def test_registration_wrong_password_no_upper_letters(browser):
    characters = string.ascii_lowercase + string.digits
    length = random.choice([random.randint(8, 40)])
    password = "".join(random.choice(characters) for _ in range(length))
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    registration_page = RegistrationPage(browser)
    print("\n--- Запуск теста: test_registration_wrong_password_no_upper_letters ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    auth_page.open_registration_form()
    registration_page.fill_password(password)
    registration_page.click_anywhere()

    is_form_incorrect = registration_page.is_form_incorrect()
    assert is_form_incorrect, "Форма пароля имени позволяет ввод пароля без прописных букв!"
    if is_form_incorrect:
        print("Форма ввода пароля требует ввода прописных букв!")
    print("--- Тест test_registration_wrong_password_no_upper_letters завершен ---")

# 5. Проверка пароля без строчных букв
def test_registration_wrong_password_no_lower_letters(browser):
    characters = string.ascii_uppercase + string.digits
    length = random.choice([random.randint(8, 40)])
    password = "".join(random.choice(characters) for _ in range(length))
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    registration_page = RegistrationPage(browser)
    print("\n--- Запуск теста: test_registration_wrong_password_no_lower_letters ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    auth_page.open_registration_form()
    registration_page.fill_password(password)
    registration_page.click_anywhere()

    is_form_incorrect = registration_page.is_form_incorrect()
    assert is_form_incorrect, "Форма пароля имени позволяет ввод пароля без строчных букв!"
    if is_form_incorrect:
        print("Форма ввода пароля требует ввода строчных букв!")
    print("--- Тест test_registration_wrong_password_no_lower_letters завершен ---")

# 6. Проверка кнопки "Показать пароль"
def test_show_password(browser):
    password = "TesT012345678"
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    registration_page = RegistrationPage(browser)
    print("\n--- Запуск теста: test_show_password ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    auth_page.open_registration_form()
    registration_page.fill_password(password)
    assert (
            registration_page.get_password_field_type() == "password"
    ), "Пароль открыт изначально!"
    registration_page.click_show_password_btn()
    current_type = registration_page.get_password_field_type()
    assert (
            current_type == "text"
    ), f"Ожидался тип 'text', но получен '{current_type}'!"
    print("Нажатие кнопки 'Показать пароль' показывает пароль!")
    print("--- Тест test_show_password завершен ---")

# 7. Проверка ввода несуществующего региона
def test_wrong_region(browser):
    region = 'Бутербродная губерния'
    auth_page = AuthPage(browser, url=Settings.BASE_URL)
    registration_page = RegistrationPage(browser)
    print("\n--- Запуск теста: test_wrong_region ---")
    auth_page.open()
    auth_page.choose_auth_by_password()
    auth_page.open_registration_form()
    registration_page.fill_region(region)
    is_wrong_region = registration_page.get_region_error_message()
    assert is_wrong_region, "Возможен ввод несуществующего региона!"
    if is_wrong_region:
        print("Ввод несуществующего региона невозможен!")
        print("--- Тест test_wrong_region завершен ---")