from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

_driver = webdriver.Firefox()
_driver.get('https://phptravels.com/demo/')


_driver.find_element(By.NAME, 'first_name').send_keys('Alfredo')
_driver.find_element(By.NAME, 'last_name').send_keys('Lobo')
_driver.find_element(By.NAME, 'business_name').send_keys('gambiarras clube')
_driver.find_element(By.NAME, 'email').send_keys('gamgiarrasclube.com.br')
number1 = _driver.find_element(By.ID, 'numb1').text
number2 = _driver.find_element(By.ID, 'numb2').text
n1 = int(number1)
n2 = int(number2)
sum = n1 + n2
result = _driver.find_element(By.ID, 'number').send_keys(sum)
_driver.find_element(By.ID, 'demo').click()



