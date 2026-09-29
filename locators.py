from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")   # Кнопка «Войти в аккаунт» по центру главной
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")        # Ссылка «Личный Кабинет» в хедере
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")                # Ссылка «Конструктор» в хедере
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")    # Логотип Stellar Burgers
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")            # Кнопка «Оформить заказ» — признак авторизации

    # Вкладки конструктора
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")

    # Активная вкладка — у выбранной вкладки появляется класс tab_tab_type_current
    BUNS_TAB_ACTIVE = (By.XPATH, "//span[text()='Булки']/parent::div[contains(@class, 'tab_tab_type_current')]")
    SAUCES_TAB_ACTIVE = (By.XPATH, "//span[text()='Соусы']/parent::div[contains(@class, 'tab_tab_type_current')]")
    FILLINGS_TAB_ACTIVE = (By.XPATH, "//span[text()='Начинки']/parent::div[contains(@class, 'tab_tab_type_current')]")

    # Заголовки разделов — для проверки скролла
    BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")                            # Ссылка «Войти» внизу формы регистрации
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")          # Ошибка под полем пароля
    REGISTRATION_PAGE_TITLE = (By.XPATH, "//h2[text()='Регистрация']")


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")            # Ссылка на регистрацию
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")    # Ссылка на восстановление пароля
    LOGIN_PAGE_TITLE = (By.XPATH, "//h2[text()='Вход']")


class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")                            # Ссылка «Войти» в форме восстановления


class AccountPageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")                        # Признак, что мы в ЛК
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")                    # Кнопка выхода