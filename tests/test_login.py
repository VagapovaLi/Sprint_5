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

    def test_button_login_account(self):
        Auth.login(self.driver, email='liana@mail.ru', password='123456', use_personal_account=False)

    def test_login_personal_account(self):
        Auth.login(self.driver, email='liana@mail.ru', password='123456', use_personal_account=True)

    def test_registration(self):
        Auth.register(self.driver, email='liana@mail.ru', password='123456')

    def test_recover_password(self):
        Auth.recover_password(self.driver, email='liana@mail.ru')



