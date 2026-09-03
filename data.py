import random
import string

class Urls:
    BASE_URL = 'https://stellarburgers.education-services.ru'
    MAIN_PAGE = BASE_URL + '/'
    LOGIN_PAGE = BASE_URL + '/login'
    REGISTER_PAGE = BASE_URL + '/register'
    FORGOT_PASSWORD_PAGE = BASE_URL + '/forgot-password'
    ACCOUNT_PAGE = BASE_URL + '/account/profile'

def generate_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f'simdmitriy_{random_string}@yandex.ru'


def generate_password():
    return ''.join(random.choices(string.digits, k=6))


# Учётные данные существующего тестового аккаунта
USER_EMAIL = 'simdmitriy_54_999@yandex.ru'
USER_PASSWORD = '12345678'
