from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import USER_EMAIL, USER_PASSWORD
from locators import MainPageLocators, LoginPageLocators, AccountPageLocators


class TestLogout:
    def test_logout_from_personal_account(self, driver):
        wait = WebDriverWait(driver, 5)

        # Переход в личный кабинет
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()

        # Вход в аккаунт
        wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_PAGE_TITLE))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        # Ожидание завершения авторизации: ссылка «Личный Кабинет» есть и на странице входа,
        # поэтому кликать по ней можно только после появления кнопки «Оформить заказ»
        wait.until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)).click()

        # Выход из личного аккаунта
        wait.until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()

        # Проверка выхода из личного аккаунта и перехода на страницу авторизации
        login_page_title = wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_PAGE_TITLE))
        assert login_page_title.is_displayed()
