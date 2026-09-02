from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators


class TestSwitchSectionInConstructor:
    def test_switch_section_in_constructor(self, driver):
        wait = WebDriverWait(driver, 5)

        # Переход и нажатие на раздел "Начинки"
        wait.until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)).click()
        fillings_section = wait.until(EC.visibility_of_element_located(MainPageLocators.FILLINGS_TAB_ACTIVE))
        assert fillings_section.is_displayed()

        # Переход и нажатие на раздел "Соусы"
        wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()
        sauces_section = wait.until(EC.visibility_of_element_located(MainPageLocators.SAUCES_TAB_ACTIVE))
        assert sauces_section.is_displayed()

        # Переход и нажатие на раздел "Булки"
        wait.until(EC.element_to_be_clickable(MainPageLocators.BUNS_TAB)).click()
        buns_section = wait.until(EC.visibility_of_element_located(MainPageLocators.BUNS_TAB_ACTIVE))
        assert buns_section.is_displayed()
