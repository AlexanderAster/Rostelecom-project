from selenium.webdriver.common.by import By
# Поиск осуществляется в реальном времени по ID/CLASS_NAME/XPATH/NAME. (Могут измениться)
class RegisterLocators: # Класс локаторов. 
    '''Далее локаторы для страницы регистрации. Используются в тестах формы регистрации'''
    NAME = (By.NAME, "firstName") # локатор поля имени.    
    SURNAME = (By.NAME, "lastName") # локатор поля фамилии
    ADDRESS = (By.ID, "address") # локатор поля email или телефона
    PASS = (By.ID, "password") # локатор поля пароля
    PASSCONF = (By.ID, "password-confirm") # локатор поля подтверждения пароля
    REG_BTN = (By.NAME, "register") # локатор кнопки (зарегистрироваться)
    ERROR_NAME = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/span')# Ошибка под полем имени
    ERROR_SURNAME = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span')# Ошибка под полем фамилии
    ERROR_ADDRESS = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[3]/div/span')# Ошибка под полем mail/phone
    ERROR_PASS = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[1]/span')# Ошибка под полем пароля
    ERROR_PASSCONF = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[4]/div[2]/span')# Ошибка под полем подтверждения пароля
    CHANGE_MAIL = (By.NAME, 'otp_back_phone') # локатор кнопки "изменить email"
    CONFIRM_REG = (By.NAME, 'registration_confirm_btn') # локатор кнопки подтверждения регистрации. (Для случая,если адрес занят)
    HEADER_HOME = (By.XPATH, '//div[contains(@class, "home")]')# Локатор страницы личного кабинета. (Для проверки,что пользователь вошёл)
class AuthorizationLocators:
    '''Далее локаторы формы авторизации. Используются в тестах страницы авторизации'''
    TAB_EMAIL = (By.ID, 't-btn-tab-mail')# Переход на вкладку аутентификации через почту
    TAB_LOGIN = (By.ID, 't-btn-tab-login')# Переход на вкладку аутентификации через логин
    TAB_PERACC = (By.ID, 't-btn-tab-ls')# Переход на вкладку аутентификации через лицевой счёт
    LOGIN = (By.ID, 'username')# локатор поля логина/почты/телефона/лицевого счёта. Идентичен для всех вкладок
    PASS = (By.ID, 'password')# локатор для поля пароля. Идентичен для всех вкладок
    AUTH_BTN = (By.ID, 'kc-login')# локатор кнопки "Войти"
    AUTH_REG = (By.ID, 'kc-register')# локатор кнопки "Зарегистрироваться"
    VK_ICON = (By.ID, 'oidc_vk')# локатор иконки Вконтакте
    OK_ICON = (By.ID, 'oidc_ok')# локатор иконки Одноклассники
    MAIL_ICON = (By.ID, 'oidc_mail')# локатор иконки Mail.ru
    YA_ICON = (By.ID, 'oidc_ya')# локатор иконки Яндекс ID
    ERROR_FIELD = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/span') # ошибка под полем username
    ERROR_MESSAGE = (By.ID, 'form-error-message')# ошибка над формой авторизации. Главное сообщение
    RESET_PASS_BTN = (By.ID, 'forgot_password')# локатор кнопки "Забыл пароль"
    PICTURE_CODE = (By.NAME, 'code') # Локатор поля символов с картинки
class ResetPasswordLocators:
    CONTINUE_BTN = (By.ID, 'reset')# локатор кнопки "Продолжить"
    CODE_FIELD = (By.XPATH, '//*[@id="rt-code-0"]') # Локатор поля для ввода проверочного кода
class AuthCodeLocators:
    LOGIN = (By.ID, "address") # локатор поля адреса
    HEADER_REDIRECT = (By.XPATH, '//h2[contains(text(), "Добро пожаловать")]') # локатор заголовка страницы,отображаемой при успешной авторизации
    GET_CODE_BTN = (By.ID, 'otp_get_code')# локатор кнопки "Получить код"
    ERROR_ADDRESS = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div/span')# ошибка под полем адреса