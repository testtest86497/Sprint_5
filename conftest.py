import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()                 # сработает даже если тест упал