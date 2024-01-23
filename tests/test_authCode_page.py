import pytest, time
from selenium import webdriver
from page_atributs.locators import AuthCodeLocators, RegisterLocators
from page_atributs.values import AuthValues

@pytest.fixture(autouse=True)
def driver(): # отработает в начале каждого теста
   driver = webdriver.Firefox()
   driver.implicitly_wait(10)
   driver.get('https://start.rt.ru/')
   yield driver
   driver.quit()

def test_auth_code(driver):
   '''Тест-кейс TRT-034. Позитивный сценарий авторизации через метод Авторизация по коду'''
   driver.find_element(*AuthCodeLocators.LOGIN).send_keys(*AuthValues.correct_phone) 
   driver.find_element(*AuthCodeLocators.GET_CODE_BTN).click()
   time.sleep(25)
   if driver.current_url == AuthValues.MAIN_URL: # Если аккаунт уже создан,пользователь попадёт на главную
      assert driver.current_url == AuthValues.MAIN_URL
   elif driver.find_element(*AuthCodeLocators.HEADER_REDIRECT): # Если аккаунт новый,страница приветствия и донастройки
      assert driver.find_element(*AuthCodeLocators.HEADER_REDIRECT)
   elif driver.find_element(*RegisterLocators.HEADER_HOME): # Иногда осуществляется переход в личный кабинет
      assert driver.find_element(*RegisterLocators.HEADER_HOME)