import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import time
class TestConstructor:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_go_to_section_sauces(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SECTION_SAUCE)).click()
        assert WebDriverWait(driver,3).until(
            EC.visibility_of_element_located(Locators.LABEL_SAUCES_TAB)).text == 'Соусы'

    def test_go_to_section_rolls(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SECTION_TOPPINGS)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SECTION_ROLLS)).click()

        assert WebDriverWait(driver,3).until(
            EC.visibility_of_element_located(Locators.LABEL_ROLLS_TAB)).text == 'Булки'

    def test_go_to_section_toppings(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.SECTION_TOPPINGS)).click()

        assert WebDriverWait(driver,3).until(
            EC.visibility_of_element_located(Locators.LABEL_TOPPINGS_TAB)).text == 'Начинки'
