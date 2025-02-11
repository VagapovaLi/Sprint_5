from selenium.webdriver.common.by import By

class Locators:
    BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, '//*[@id="root"]/div//section[2]//button')    #кнопкФ «Войти в аккаунт» на главной

    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]//fieldset[1]/div/div/input')             # поле ввода email
    PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]//fieldset[2]/div/div/input')           #поле ввода пароль
    BUTTON_LOGIN = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')               #кнопка Войти
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p')       #кнопка личный кабинет на главной
    BUTTON_LOGIN_REGISTER = (By.XPATH, '//*[@id="root"]/div//div//p/a')               #кнопка Войти в форме регистрации
    BUTTON_RECOVER_PASSWORD = (By.XPATH, '//*[@id="root"]//p[2]/a')                   #кнопка Восстоновить пароль
    BUTTON_RECOVER_LOGIN =(By.XPATH, '//*[@id="root"]/div//p/a')                        #кнопка Войти в форме восстановления пароля

    NAME_INPUT_REG = (By.XPATH, '//*[@id="root"]//fieldset[1]/div/div/input')       # поле ввода имени в форме регистрации
    EMAIL_INPUT_REG = (By.XPATH, '//*[@id="root"]//fieldset[2]/div/div/input')      # поле ввода email в форме регистрации
    PASSWORD_INPUT_REG = (By.XPATH, '//*[@id="root"]//fieldset[3]/div/div/input')   # поле ввода пароля в форме регистрации

    BUTTON_CONSTRUCTOR = (By.XPATH, '//*[@id="root"]/div//li[1]//p')                 #кнопка конструктор
    BUTTON_STELLAR_BURGERS= (By.XPATH, '//*[@id="root"]//div/a')                    #кнопка STELLAR BURGERS
    BUTTON_LOGOUT_PERSONAL_ACCOUNT=(By.XPATH,'//*[@id="root"]//div//li[3]/button')   #кнопка выход в личном кабинете

    SECTION_SAUCE = (By.XPATH,'//span[contains(text(), "Соусы")]')           #кнопка соус
    SECTION_ROLLS = (By.XPATH, '//span[contains(text(), "Булки")]')          #кнопка булки
    SECTION_TOPPINGS = (By.XPATH, '//span[contains(text(), "Начинки")]')        #кнопка начинки

    LABEL_BURGER_INGREDIENTS =(By.XPATH,'//*[@id="root"]//main/section[1]/div[2]')   # Форма с ингредиентами для бургеров
