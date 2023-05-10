from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from time import sleep

# AULA DO DIA 02/04 - TERÇA

# CRIAÇÃO DO DRIVER
browser = webdriver.Chrome()
browser.get('https://omayo.blogspot.com/')
browser.maximize_window()

wdw = WDW(browser, 10)
btn = wdw.until(visibility_of_element_located((By.ID, 'prompt')), 'Não encontrou o botão')
# btn = browser.find_element('xpath','//*[@id="prompt"]')
sleep(2)
btn.click()
sleep(2)

alert = Alert(browser)
sleep(2)
# TODO: Ei eu do futuro, por favor, sai desse jogo e olha essa linha de código! Pelo amor de Deus!
alert.send_keys('alguma coisa')
sleep(2)
alert.accept
print('passou')

browser.quit()