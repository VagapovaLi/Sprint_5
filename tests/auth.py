from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class Auth:

    @staticmethod
    def login(driver, email, password, use_personal_account=False):
        driver.get("https://stellarburgers.nomoreparties.site/")

        if use_personal_account:
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUTTON_PERSONAL_ACCOUNT))
            driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        else:
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.BUTTON_LOGIN_TO_ACCOUNT))
            driver.find_element(*Locators.BUTTON_LOGIN_TO_ACCOUNT).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    
    @staticmethod
    def register(driver, email, password):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(BUTTON_LOGIN_REGISTER))

        driver.find_element(BUTTON_LOGIN_REGISTER).click()
        driver.find_element(EMAIL_INPUT).send_keys(email)
        driver.find_element(PASSWORD_INPUT ).send_keys(password)
        driver.find_element(BUTTON_LOGIN).click()

        WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    @staticmethod
    def recover_password(driver, email, password):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(BUTTON_RECOVER_PASSWORD))
        driver.find_element(BUTTON_RECOVER_PASSWORD).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((BUTTON_RECOVER_LOGIN))
        )
        driver.find_element(BUTTON_RECOVER_LOGIN).click()

        driver.find_element(EMAIL_INPUT).send_keys(email)
        driver.find_element(PASSWORD_INPUT ).send_keys(password)
        driver.find_element(BUTTON_LOGIN).click()

        WebDriverWait(driver, 10).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
