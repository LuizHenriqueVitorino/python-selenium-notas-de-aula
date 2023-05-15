import sys
import os

# Adiciona o caminho para o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.login_page import CaixaLoginPage, CredenciaisPage
from time import sleep
from selenium import webdriver

# setUp
driver = webdriver.Chrome()
login = CaixaLoginPage(driver)
credenciais = CredenciaisPage(driver)


# Teste
login.entrar()
usuario_sucesso = credenciais.get_usuarios()[0]
senha = credenciais.get_senhas()[0]
login.logar(usuario_sucesso, senha)

# terarDown
sleep(5)
login.driver.close()

