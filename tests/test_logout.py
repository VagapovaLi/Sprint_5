from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import Locators
from auth import Auth
import unittest

class TestAuth(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

def test_logout_by_bytton_logout(self):
    Auth.login(self.driver, email='liana@mail.ru', password='123456', use_personal_account=False)

    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.BUTTON_LOGOUT_PERSONAL_ACCOUNT).click()