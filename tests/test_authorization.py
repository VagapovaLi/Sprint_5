import pytest
from selenium import webdriver
from helper import Auth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import time
BASE_URL = "https://stellarburgers.nomoreparties.site"

class TestAuth:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_button_login_account(self, driver):
        Auth.login(driver, email='liana@mail.ru', password='123456', use_personal_account=True)

        assert WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.BUTTON_PLACE_ORDER))

    def test_login_personal_account(self, driver):
        Auth.login(driver,email='liana@mail.ru', password='123456', use_personal_account=False)

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.BUTTON_PLACE_ORDER))

    def test_login_in_the_registration_(self, driver):
        Auth.register(driver, email='liana@mail.ru', password='123456')

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.BUTTON_PLACE_ORDER))


    def test_login_recover_password(self, driver):
        Auth.recover_password(driver, email='liana@mail.ru')

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.TEXT_PASSWORD_RECOVER))
