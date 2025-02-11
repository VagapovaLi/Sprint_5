import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

#переход по клику на «Личный кабинет
def test_button_login_account(self):
    Auth.login(self.driver, email='liana@mail.ru', password='123456', use_personal_account=False)

    driver.find_element(BUTTON_PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'




