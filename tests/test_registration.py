from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, RegisterPageLocators, LoginPageLocators
from data import Urls, generate_email, generate_password


class TestRegistration:

    def test_success_registration_with_valid_data(self, driver):
        wait = WebDriverWait(driver, 5)
        email = generate_email()
        password = generate_password()

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()

        wait.until(EC.visibility_of_element_located(RegisterPageLocators.REGISTRATION_PAGE_TITLE))

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys('test')
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        login_page_title = wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_PAGE_TITLE))
        assert login_page_title.text == 'Вход'
        assert driver.current_url == Urls.LOGIN_PAGE


    def test_registration_with_not_valid_password(self, driver):
        wait = WebDriverWait(driver, 5)
        email = generate_email()

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()

        wait.until(EC.visibility_of_element_located(RegisterPageLocators.REGISTRATION_PAGE_TITLE))

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys('test')
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys('11111')
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        password_error = wait.until(EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR))
        assert password_error.text == 'Некорректный пароль'
        assert driver.current_url == Urls.REGISTER_PAGE