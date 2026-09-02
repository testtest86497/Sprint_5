from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import USER_EMAIL, USER_PASSWORD
from locators import MainPageLocators, LoginPageLocators, AccountPageLocators


class TestNavigate:
    def test_navigate_to_personal_account_from_main_page(self, driver):
        wait = WebDriverWait(driver, 5)

        # Переход в личный кабинет
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()

        # Проверка перехода на страницу авторизации
        login_page_title = wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_PAGE_TITLE))
        assert login_page_title.is_displayed()

    def test_navigate_to_constructor_from_personal_account(self, driver):
        wait = WebDriverWait(driver, 5)

        # Переход в личный кабинет
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()

        # Вход в аккаунт: без авторизации личный кабинет не открыть
        wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_PAGE_TITLE))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()
        wait.until(EC.visibility_of_element_located(AccountPageLocators.PROFILE_LINK))

        # Переход в конструктор
        driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()

        # Проверка перехода на страницу с конструктором
        main_page = wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        assert main_page.is_displayed()
