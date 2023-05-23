from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração (setUp)
driver = webdriver.Chrome()
wdw = WebDriverWait(driver, 60)
driver.maximize_window()
driver.get("https://prpi.ifce.edu.br/nl/app_Login/")

# Realizar Login
driver.find_element(By.ID, "id_sc_field_login").send_keys("60435252321")
driver.find_element(By.ID, "id_sc_field_pswd").send_keys("147896325")
wdw.until(EC.element_to_be_clickable((By.CLASS_NAME, "button")))
driver.find_element(By.CLASS_NAME, "button").click()

# Mudando para outro frame
wdw.until(EC.presence_of_element_located((By.ID, "iframe_MenuPrincipal")), "Frame não encontrado!")
driver.switch_to.frame(driver.find_element(By.ID, "iframe_MenuPrincipal"))