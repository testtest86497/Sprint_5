from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import Urls, USER_EMAIL, USER_PASSWORD
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, ForgotPasswordPageLocators


class TestLogin:
    def test_login_via_login_button(self, driver):
        wait = WebDriverWait(driver, 5)

        wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_ACCOUNT_BUTTON)).click()

        # Вход в аккаунт
        wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_PAGE_TITLE))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Проверка перехода на главную страницу
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert driver.current_url == Urls.MAIN_PAGE


    def test_login_via_personal_account_button(self, driver):
        wait = WebDriverWait(driver, 5)

        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()

        # Вход в аккаунт
        wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_PAGE_TITLE))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Проверка перехода на главную страницу
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert driver.current_url == Urls.MAIN_PAGE


    def test_login_via_login_button_on_the_registration_page(self, driver):
        wait = WebDriverWait(driver, 5)

        # Переход по линку войти в аккаунт, на странице регистрации
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.element_to_be_clickable(LoginPageLocators.REGISTER_LINK)).click()
        wait.until(EC.url_to_be(Urls.REGISTER_PAGE))
        wait.until(EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK)).click()

        # Вход в аккаунт
        wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_PAGE_TITLE))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Проверка перехода на главную страницу
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert driver.current_url == Urls.MAIN_PAGE


    def test_login_via_the_forgot_password(self, driver):
        wait = WebDriverWait(driver, 5)

        # Переход по линку войти в аккаунт, на странице забыли пароль
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)).click()
        wait.until(EC.url_to_be(Urls.FORGOT_PASSWORD_PAGE))
        wait.until(EC.element_to_be_clickable(ForgotPasswordPageLocators.LOGIN_LINK)).click()

        # Вход в аккаунт
        wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_PAGE_TITLE))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Проверка перехода на главную страницу
        assert wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert driver.current_url == Urls.MAIN_PAGE
