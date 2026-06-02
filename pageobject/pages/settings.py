import os
from dotenv import load_dotenv

# Переменные из файла .env
load_dotenv()


class Settings:
    # Базовые настройки
    BASE_URL = os.getenv("BASE_URL", "https://lk.rt.ru")
    RESET_CREDENTIALS_URL = os.getenv("RESET_CREDENTIALS_URL", 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials')

    # Учетные данные (обязательно через переменные окружения)
    LOGIN = os.getenv("RT_LOGIN", "default_user")
    PASSWORD = os.getenv("RT_PASSWORD", "default_password")

    # Тестовые данные
    INVALID_LOGIN = "invalid_user@mail.ru"
    INVALID_PASSWORD = "WrongPassword123"
    DUMMY_CAPTCHA = "WRONG123"
    REGION = 'Санкт-Петербург г'

    # Тайм-ауты
    DEFAULT_TIMEOUT = 10
    LONG_TIMEOUT = 30