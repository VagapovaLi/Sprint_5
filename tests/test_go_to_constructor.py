import pytest
from selenium import webdriver
from helper import Auth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestAuth:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_click_on_constructor(self, driver):
        Auth.login(driver, email='liana@mail.ru', password='123456', use_personal_account=True)

        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()

        assert WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.BUTTON_PLACE_ORDER))


    def test_click_on_stellar_burgers(self, driver):
        Auth.login(driver, email='liana@mail.ru', password='123456', use_personal_account=True)

        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_STELLAR_BURGERS).click()

        assert WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.BUTTON_PLACE_ORDER))