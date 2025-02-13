import pytest
from selenium import webdriver
from helper import Auth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import time

LOGIN_URL = "https://stellarburgers.nomoreparties.site/login"
class TestAuth:

    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()


    def test_logout_byt_logout(self,driver):
        Auth.login(driver, email='liana@mail.ru', password='123456', use_personal_account=True)

        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.BUTTON_LOGOUT_PERSONAL_ACCOUNT)).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL
