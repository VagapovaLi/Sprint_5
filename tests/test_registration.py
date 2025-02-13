import pytest
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
BASE_URL = "https://stellarburgers.nomoreparties.site"
REGISTER_URL = f"{BASE_URL}/register"
LOGIN_URL = f"{BASE_URL}/login"

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def create_random_user(cls):
        name = 'testname'
        random_email = f"Лиана_Тихонова_18{random.randint(100, 999)}@yandex.ru"
        random_password = random.randint(100000, 999999)
        return cls(name, random_email, random_password)

@pytest.fixture
def user_fixture():
    user = User.create_random_user()
    return user

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_registration(driver, user_fixture):
    driver.get(REGISTER_URL)

    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.NAME_INPUT_REG)).send_keys(user_fixture.name)
    driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(user_fixture.email)
    driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(user_fixture.password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
    assert driver.current_url == LOGIN_URL

def test_registration_with_error(driver, user_fixture):
    driver.get(REGISTER_URL)
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.NAME_INPUT_REG)).send_keys(user_fixture.name)
    driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(user_fixture.email)
    driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(12345)
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    error_message = driver.find_element(*Locators.TEXT_ERROR_INCORRECT_PASSWORD)
    assert error_message.is_displayed()
