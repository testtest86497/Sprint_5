import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.education-services.ru/')
    yield driver
    driver.quit()                 # сработает даже если тест упал