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

    def test_go_to_section_sauces(self):
        Auth.login(self.driver, email='liana@mail.ru', password='123456', use_personal_account=False)
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.SECTION_SAUCE).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LABEL_BURGER_INGREDIENTS)).text == 'Соусы'

    def test_go_to_section_rolls(self):
        Auth.login(self.driver, email='liana@mail.ru', password='123456', use_personal_account=False)
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.SECTION_ROLLS).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LABEL_BURGER_INGREDIENTS)).text == 'Булки'

    def test_go_to_section_toppings(self):
        Auth.login(self.driver, email='liana@mail.ru', password='123456', use_personal_account=False)
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.SECTION_TOPPINGS).click()

        assert WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LABEL_BURGER_INGREDIENTS)).text == 'Начинки'