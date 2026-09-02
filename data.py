import random
import string


def generate_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f'simdmitriy_{random_string}@yandex.ru'


def generate_password():
    return ''.join(random.choices(string.digits, k=6))


# Учётные данные существующего тестового аккаунта
USER_EMAIL = 'simdmitriy_54_999@yandex.ru'
USER_PASSWORD = '12345678'
