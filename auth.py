
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window() # полноэкранный режим
driver.get('https://agro-management.itcase.pro/auth/') #переходим на страницу авторизации

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@data-test-id='usernameFieldInput']"))).send_keys('test@itcase.pro')
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@data-test-id='passwordFieldInput']"))).send_keys('Ki2gxM75QrdDuNH9')
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@data-test-id='submitButton']"))).click()

time.sleep(3)
current_url = driver.current_url #получаем адрес текущей страницы
#print(current_url)
def test():
   assert current_url == 'https://agro-management.itcase.pro/' # проверяем что адрес текущей страницы соответсвует главной после входа

