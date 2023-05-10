from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# AULA DO DIA 02/04 - TERÇA

# CRIAÇÃO DO DRIVER E CONFIGURAÇÕES
driver = webdriver.Chrome()
wdw = WebDriverWait(driver, 10)
driver.get('https://omayo.blogspot.com/')
driver.maximize_window()

# CLICA NO BOTÃO DO PROMPT
botao = wdw.until(EC.element_to_be_clickable((By.ID, 'prompt')), "Deu ruim com o prompt")
botao.click()

# INTERAÇÃO COM O ALERTA
alert = Alert(driver)
sleep(5)
alert.send_keys('alguma coisa bem legal!')
alert.accept()
