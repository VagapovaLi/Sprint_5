import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from auth import Auth
import unittest
from locators import Locators


class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

def test_click_on_constructor(self):
    Auth.login(self.driver, email='liana@mail.ru', password='123456', use_personal_account=False)

    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()

    WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

def test_click_on_stellar_burgers(self):
    Auth.login(self.driver, email='liana@mail.ru', password='123456', use_personal_account=False)

    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.BUTTON_STELLAR_BURGERS).click()

    WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
