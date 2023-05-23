from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.switch_to.frame(driver.find_element(By.ID, "iframe_MenuPrincipal"))