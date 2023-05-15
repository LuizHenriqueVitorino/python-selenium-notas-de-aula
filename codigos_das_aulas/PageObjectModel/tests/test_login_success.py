import sys
import os

# Adicione o caminho para o diretório raiz do seu projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import CaixaLogin
from time import sleep
from selenium import webdriver

# setUp
driver = webdriver.Chrome()
pagina = CaixaLogin(driver)

# Teste
pagina.entrar()
pagina.logar('standard_user', 'secret_sauce')

# terarDown
sleep(5)
pagina.driver.close()

