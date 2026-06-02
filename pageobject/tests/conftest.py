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