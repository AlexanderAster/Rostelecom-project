import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By # для компактности кода и сокращений By.ID/XPATH
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_atributs.locators import AuthorizationLocators, ResetPasswordLocators, RegisterLocators
from page_atributs.values import AuthValues

@pytest.fixture(autouse=True,scope='session') # scope session прогонит код фикстуры один раз за весь прогон
def driver():
   driver = webdriver.Firefox()
   driver.implicitly_wait(10)
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   yield driver
   driver.quit()
@pytest.fixture(scope='function') # фикстура для каждого теста
def close(): # метод закрытия активного окна. 
   driver.close()

def test_pozitive_auth(driver):
   '''Тест-кейс TRT-036. Проверка авторизации с валидными данными'''
   driver.find_element(*AuthorizationLocators.LOGIN).send_keys(*AuthValues.correct_phone)
   driver.find_element(*AuthorizationLocators.PASS).send_keys(*AuthValues.correct_pass)
   time.sleep(1)
   driver.find_element(*AuthorizationLocators.AUTH_BTN).click()  
   assert driver.find_element(*RegisterLocators.HEADER_HOME)
   close
def testAuth_wrong_passPHONE(driver):
   '''Тест-кейс TRT-020. Попытка входа с неверным паролем. Аутентификация через телефон'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.LOGIN).send_keys(*AuthValues.correct_phone)
   driver.find_element(*AuthorizationLocators.PASS).send_keys(*AuthValues.wrong_pass)
   time.sleep(1)
   driver.find_element(*AuthorizationLocators.AUTH_BTN).click()  
   assert driver.find_element(*AuthorizationLocators.ERROR_MESSAGE)
   close
def testAuth_wrong_passMAIL(driver):
   '''Тест-кейс TRT-021. Попытка входа с неверным паролем. Аутентификация через почту'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.TAB_EMAIL).click() # переход к вкладке авторизации через почту
   driver.find_element(*AuthorizationLocators.LOGIN).send_keys(*AuthValues.correct_email)
   driver.find_element(*AuthorizationLocators.PASS).send_keys(*AuthValues.wrong_pass)
   time.sleep(1)
   driver.find_element(*AuthorizationLocators.AUTH_BTN).click()  
   assert driver.find_element(*AuthorizationLocators.ERROR_MESSAGE)
   close
def testAuth_wrong_passLOGIN(driver):
   '''Тест-кейс TRT-022. Попытка входа с неверным паролем. Аутентификация через логин'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.TAB_LOGIN).click() 
   driver.find_element(*AuthorizationLocators.LOGIN).send_keys(*AuthValues.correct_login)
   driver.find_element(*AuthorizationLocators.PASS).send_keys(*AuthValues.wrong_pass)
   time.sleep(1)
   driver.find_element(*AuthorizationLocators.AUTH_BTN).click()  
   assert driver.find_element(*AuthorizationLocators.ERROR_MESSAGE)
   close
def testAuth_wrong_passLS(driver):
   '''Тест-кейс TRT-023. Попытка входа с неверным паролем. Аутентификация через лицевой счёт'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.TAB_PERACC).click() 
   driver.find_element(*AuthorizationLocators.LOGIN).send_keys(*AuthValues.correct_ls)
   driver.find_element(*AuthorizationLocators.PASS).send_keys(*AuthValues.wrong_pass)
   time.sleep(1)
   driver.find_element(*AuthorizationLocators.AUTH_BTN).click()  
   assert driver.find_element(*AuthorizationLocators.ERROR_MESSAGE)
   close
def test_error_phone(driver):
   '''Тест-кейс TRT-024. Проверка отображения ошибки под полем Телефон'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.LOGIN).send_keys(*AuthValues.wrong_phone)
   time.sleep(1)
   driver.find_element(*AuthorizationLocators.AUTH_BTN).click()  
   assert driver.find_element(*AuthorizationLocators.ERROR_FIELD)
   close
def test_error_email(driver):
   '''Тест-кейс TRT-025. Проверка отображения ошибки под полем Электронная почта"'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.TAB_EMAIL).click() 
   driver.find_element(*AuthorizationLocators.AUTH_BTN).click()  
   assert driver.find_element(*AuthorizationLocators.ERROR_FIELD)
   close
def test_error_login(driver):
   '''Тест-кейс TRT-026. Проверка отображения ошибки под полем Логин'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.TAB_LOGIN).click() 
   driver.find_element(*AuthorizationLocators.AUTH_BTN).click()  
   assert driver.find_element(*AuthorizationLocators.ERROR_FIELD)
   close
def test_error_ls(driver):
   '''Тест-кейс TRT-027. Проверка отображения ошибки под полем Лицевой счёт'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.TAB_PERACC).click() 
   driver.find_element(*AuthorizationLocators.LOGIN).send_keys(*AuthValues.wrong_ls)
   time.sleep(1) 
   driver.find_element(*AuthorizationLocators.AUTH_BTN).click()  
   assert driver.find_element(*AuthorizationLocators.ERROR_FIELD)
   close
def test_wrong_code(driver):
   '''Тест-кейс TRT-32 . Проверка возможности сбросить пароль,используя случайный проверочный код'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.RESET_PASS_BTN).click()
   driver.find_element(*AuthorizationLocators.LOGIN).send_keys(*AuthValues.correct_phone)
   wait = WebDriverWait(driver,30)
   if driver.find_element(*AuthorizationLocators.PICTURE_CODE):# Если система требует ввода символов с картинки
      wait.until(EC.presence_of_element_located((ResetPasswordLocators.CODE_FIELD))) # Тест ожидает перехода к следующему шагу
   else: # Если система не требует ввода символов - переход к следующему шагу автоматически
      driver.find_element(*ResetPasswordLocators.CONTINUE_BTN).click()
   driver.find_element(*ResetPasswordLocators.CODE_FIELD).send_keys(*AuthValues.random_sms_code)
   assert driver.find_element(*AuthorizationLocators.ERROR_MESSAGE)
   close
def test_sendCode_unregMail(driver):
   '''Тест-кейс TRT-33. Проверка возможности отправить проверочный код на незарегистрированный адрес'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.RESET_PASS_BTN).click()
   driver.find_element(*AuthorizationLocators.TAB_EMAIL).click()
   driver.find_element(*AuthorizationLocators.LOGIN).send_keys(*AuthValues.wrong_email)
   wait = WebDriverWait(driver,30)
   if driver.find_element(*AuthorizationLocators.PICTURE_CODE):
      wait.until(EC.presence_of_element_located((AuthorizationLocators.ERROR_MESSAGE))) 
   else: 
      driver.find_element(*ResetPasswordLocators.CONTINUE_BTN).click()
   assert driver.find_element(*AuthorizationLocators.ERROR_MESSAGE)
   close
def test_vk_icon(driver):
   '''Тест-кейс TRT-028. Проверка функциональности ссылки объекта: иконка ВКонтакте'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.VK_ICON).click()
   assert driver.find_element(By.XPATH, '//div[contains(@class, "vkc__ServiceAvatar__serviceAvatar")]')
   close
def test_ok_icon(driver):
   '''Тест-кейс TRT-029. Проверка функциональности ссылки объекта: иконка Одноклассники'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.OK_ICON).click()
   assert driver.find_element(By.XPATH, '//*[@id="widget-el"]/div[2]/div/div/div[4]')
   close
def test_mail_icon(driver):
   '''Тест-кейс TRT-030. Проверка функциональности ссылки объекта: иконка почты Mail.ru'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.MAIL_ICON).click()
   assert driver.find_element(By.XPATH, '//*[@id="wrp"]/div[1]/span')
   close
def test_yandx_icon(driver):
   '''Тест-кейс TRT-031. Проверка функциональности ссылки объекта: иконка яндекс ID'''
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   driver.find_element(*AuthorizationLocators.YA_ICON).click()
   assert driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/a')