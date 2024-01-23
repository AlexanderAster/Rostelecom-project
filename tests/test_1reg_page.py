import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By # для компактности кода и сокращений By.ID/XPATH
from page_atributs.locators import RegisterLocators, AuthorizationLocators
from page_atributs.values import RegValues

@pytest.fixture(autouse=True)
def driver(): # отработает в начале каждого теста
   driver = webdriver.Firefox()
   driver.implicitly_wait(10)
   driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=054109ff-a399-4999-a5fa-5953cf11d093&theme&auth_type')
   yield driver
   driver.quit()
   
def test_name_min(driver):
   '''Тест-кейс TRT-001. Минимальное значение поля Имя'''
   # Попасть на форму регистрации можно лишь через форму авторизации,поскольку страница регистрации процедурно -
   # - генерирует свой временный адрес/токен.
   driver.find_element(*AuthorizationLocators.AUTH_REG).click() # переходим из формы авторизации на форму регистрации
   driver.find_element(*RegisterLocators.NAME).send_keys(*RegValues.small_name) # вставить в поле имени значение
   driver.find_element(By.XPATH, '//body').click() # кликнуть по пустому пространству,что бы страница обработала поле и выдала ошибку 
   assert driver.find_element(*RegisterLocators.ERROR_NAME) # Ожидаем ошибку под полем
def test_surname_min(driver):
   '''Тест-кейс TRT-002. Минимальное значение поля Фамилия'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.SURNAME).send_keys(*RegValues.small_surname)
   driver.find_element(By.XPATH, '//body').click()  
   assert driver.find_element(*RegisterLocators.ERROR_SURNAME)
def test_password_min(driver):
   '''Тест-кейс TRT-003. Минимальное значение поля Пароль'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.PASS).send_keys(*RegValues.small_pass)
   driver.find_element(By.XPATH, '//body').click()  
   assert driver.find_element(*RegisterLocators.ERROR_PASS)
def test_pass_confirm(driver):
   '''Тест-кейс TRT-004. Проверка зависимости полей с паролями'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.PASS).send_keys(*RegValues.correct_pass)
   driver.find_element(*RegisterLocators.PASSCONF).send_keys(*RegValues.correct_pass2)
   driver.find_element(*RegisterLocators.REG_BTN).click()
   assert driver.find_element(*RegisterLocators.ERROR_PASSCONF)
def test_name_max(driver):
   '''Тест-кейс TRT-005. Максимальное значение поля Имя'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.NAME).send_keys(*RegValues.big_name)
   driver.find_element(By.XPATH, '//body').click()  
   assert driver.find_element(*RegisterLocators.ERROR_NAME)
def test_surname_max(driver):
   '''Тест-кейс TRT-006. Максимальное значение поля Фамилия'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.SURNAME).send_keys(*RegValues.big_surname)
   driver.find_element(By.XPATH, '//body').click()  
   assert driver.find_element(*RegisterLocators.ERROR_SURNAME)
def test_password_max(driver):
   '''Тест-кейс TRT-007. Максимальное значение поля Пароль'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.PASS).send_keys(*RegValues.big_pass)
   driver.find_element(By.XPATH, '//body').click()  
   assert driver.find_element(*RegisterLocators.ERROR_PASS)
def test_name_codingENG(driver):
   '''Тест-кейс TRT-008. Проверка поля Имени на приём латинской кодировки'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.NAME).send_keys(*RegValues.eng_name)
   driver.find_element(By.XPATH, '//body').click() 
   assert driver.find_element(*RegisterLocators.ERROR_NAME)
def test_surname_codingENG(driver):
   '''Тест-кейс TRT-009. Проверка поля Фамилии на приём латинской кодировки'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.SURNAME).send_keys(*RegValues.eng_surname)
   driver.find_element(By.XPATH, '//body').click() 
   assert driver.find_element(*RegisterLocators.ERROR_SURNAME)
def test_password_codingRUS(driver):
   '''Тест-кейс TRT-010. Проверка поля пароля на приём кириллической кодировки'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.PASS).send_keys(*RegValues.rus_pass)
   driver.find_element(By.XPATH, '//body').click()  
   assert driver.find_element(*RegisterLocators.ERROR_PASS)
def test_password_onlyNUM(driver):
   '''Тест-кейс TRT-011. Проверка поля пароля на приём значения из чисел'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.PASS).send_keys(*RegValues.only_number_pass)
   driver.find_element(By.XPATH, '//body').click()  
   assert driver.find_element(*RegisterLocators.ERROR_PASS)
def test_password_onlyTXT(driver):
   '''Тест-кейс TRT-012. Проверка поля пароля на приём значения из текста'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.PASS).send_keys(*RegValues.only_text_pass)
   driver.find_element(By.XPATH, '//body').click()  
   assert driver.find_element(*RegisterLocators.ERROR_PASS)
def test_address_wrong_number(driver):
   '''Тест-кейс TRT-013. Проверка поля Email/Телефон на приём неполного номера'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.ADDRESS).send_keys(*RegValues.small_phone)
   driver.find_element(By.XPATH, '//body').click()  
   assert driver.find_element(*RegisterLocators.ERROR_ADDRESS)
def test_name_codingSPL(driver):
   '''Тест-кейс TRT-014. Проверка поля Имени на приём специальной кодировки'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.NAME).send_keys(*RegValues.special_coding_name)
   driver.find_element(By.XPATH, '//body').click()  
   assert driver.find_element(*RegisterLocators.ERROR_NAME)
def test_surname_codingSPL(driver):
   '''Тест-кейс TRT-015. Проверка поля Фамилии на приём специальной кодировки'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.SURNAME).send_keys(*RegValues.special_coding_surname)
   driver.find_element(By.XPATH, '//body').click()  
   assert driver.find_element(*RegisterLocators.ERROR_SURNAME)
def test_register_wrong_mail(driver):
   '''Тест-кейс TRT-016. Проверка возможности регистрации с ложным адресом почты'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.NAME).send_keys(*RegValues.correct_name)
   driver.find_element(*RegisterLocators.SURNAME).send_keys(*RegValues.correct_surname)
   driver.find_element(*RegisterLocators.ADDRESS).send_keys(*RegValues.wrong_email)
   driver.find_element(*RegisterLocators.PASS).send_keys(*RegValues.correct_pass)
   driver.find_element(*RegisterLocators.PASSCONF).send_keys(*RegValues.correct_pass)
   driver.find_element(*RegisterLocators.REG_BTN).click()
   assert driver.find_element(*RegisterLocators.NAME) # поскольку локатор предполагаемой ошибки неизвестен,проверяем -
   # - что мы остались на странице регистрации, путём обнаружения локатора одного из полей заполнения.
def test_register_wrong_names(driver):
   '''Тест-кейс TRT-017. Проверка возможности регистрации с нарушением в полях ФИО'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.NAME).send_keys(*RegValues.eng_name)
   driver.find_element(*RegisterLocators.SURNAME).send_keys(*RegValues.special_coding_surname)
   driver.find_element(*RegisterLocators.ADDRESS).send_keys(*RegValues.correct_phone)
   driver.find_element(*RegisterLocators.PASS).send_keys(*RegValues.correct_pass)
   driver.find_element(*RegisterLocators.PASSCONF).send_keys(*RegValues.correct_pass)
   driver.find_element(*RegisterLocators.REG_BTN).click()
   assert driver.find_element(*RegisterLocators.NAME) # проверяем,что остались на форме регистрации
def test_register_wrong_pass(driver):
   '''Тест-кейс TRT-018. Проверка возможности регистрации с нарушением в поле пароля'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.NAME).send_keys(*RegValues.correct_name)
   driver.find_element(*RegisterLocators.SURNAME).send_keys(*RegValues.correct_surname)
   driver.find_element(*RegisterLocators.ADDRESS).send_keys(*RegValues.correct_phone)
   driver.find_element(*RegisterLocators.PASS).send_keys(*RegValues.rus_pass)
   driver.find_element(*RegisterLocators.PASSCONF).send_keys(*RegValues.rus_pass)
   driver.find_element(*RegisterLocators.REG_BTN).click()
   assert driver.find_element(*RegisterLocators.NAME)
def test_save_values(driver):
   '''Тест-кейс TRT-019. Проверка сохранения второстепенных данных,при возвращении к форме регистрации'''
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.NAME).send_keys(*RegValues.correct_name)
   driver.find_element(*RegisterLocators.SURNAME).send_keys(*RegValues.correct_surname)
   driver.find_element(*RegisterLocators.ADDRESS).send_keys(*RegValues.wrong_email)
   driver.find_element(*RegisterLocators.PASS).send_keys(*RegValues.correct_pass)
   driver.find_element(*RegisterLocators.PASSCONF).send_keys(*RegValues.correct_pass)
   driver.find_element(*RegisterLocators.REG_BTN).click()
   driver.find_element(*RegisterLocators.CHANGE_MAIL).click()
   # Вернувшись на форму регистрации,мы предполагаем,что все параметры,кроме паролей,будут сохранены.
   # Дозаполняем форму передачей только паролей и ожидаем,что повторная регистрация будет успешной
   driver.find_element(*RegisterLocators.PASS).send_keys(*RegValues.correct_pass)
   driver.find_element(*RegisterLocators.PASSCONF).send_keys(*RegValues.correct_pass)
   driver.find_element(*RegisterLocators.REG_BTN).click()
   # Если мы снова оказались в окне подтверждения, значит второстепенные данные уже были заполнены системой автоматически
   assert driver.find_element(*RegisterLocators.CHANGE_MAIL) 
def test_pozitive_register(driver):
   '''Тест-кейс TRT-035. Проверка регистрации с валидными значениями'''
   wait = WebDriverWait(driver,30)
   driver.find_element(*AuthorizationLocators.AUTH_REG).click()
   driver.find_element(*RegisterLocators.NAME).send_keys(*RegValues.correct_name)
   driver.find_element(*RegisterLocators.SURNAME).send_keys(*RegValues.correct_surname)
   driver.find_element(*RegisterLocators.ADDRESS).send_keys(*RegValues.correct_phone)
   driver.find_element(*RegisterLocators.PASS).send_keys(*RegValues.correct_pass)
   driver.find_element(*RegisterLocators.PASSCONF).send_keys(*RegValues.correct_pass)
   driver.find_element(*RegisterLocators.REG_BTN).click()
   if driver.find_element(*RegisterLocators.CONFIRM_REG):
      driver.find_element(*RegisterLocators.CONFIRM_REG).click()
   wait.until(EC.presence_of_element_located((RegisterLocators.HEADER_HOME))) 
   assert driver.find_element(*RegisterLocators.HEADER_HOME)