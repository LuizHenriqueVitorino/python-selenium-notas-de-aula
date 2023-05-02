from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from time import sleep

# AULA DO DIA 02/04 - TERÇA

# CRIAÇÃO DO DRIVER
driver = webdriver.Chrome()
driver.get('https://omayo.blogspot.com/')

# PREENCHIMENTO DO FORMULÁRIO
nome = driver.find_element(By.NAME, 'userid')
nome.send_keys('Ofra')

senha = driver.find_element(By.NAME, 'pswrd')
senha.send_keys('1234')

botao = driver.find_element(By.XPATH, '//*[@id="HTML42"]/div[1]/form/input[3]')
botao.click()

# INTERAÇÃO COM O ALERTA
alert = Alert(driver)

alert.accept()
# alert.send_keys('alguma coisa bem legal!')

sleep(10)