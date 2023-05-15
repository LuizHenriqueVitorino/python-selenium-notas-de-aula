from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from abc import ABC

class SeleniumPage(ABC):
    def __init__(self) -> None:
        self.webdriver = webdriver.Chrome()

    def encontrar_elemento(self, locator):
        return self.webdriver.find_element(*locator)
    
    def escrever(self, locator, str):
        self.encontrar_elemento(locator).send_keys(str)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

class SauceDemoPage(SeleniumPage):
    url = 'https://www.saucedemo.com/'

    def entrar(self) -> None:
        self.webdriver.get(self.url)

    def get_titulo(self):
        return self.encontrar_elemento((By.CLASS_NAME, "login_logo")).text
    
class CaixaLogin(SauceDemoPage):
    nome = (By.ID, "user-name")
    senha = (By.ID, "password")
    botao = (By.ID, "login-button")

    def escrever_nome(self, nome_str: str):
        self.escrever(self.nome, nome_str)

    def escrever_senha(self, senha_str: str):
        self.escrever(self.senha, senha_str)
    
    def submit(self):
        self.clicar(self.botao)

    def logar(self, nome_user, senha_user):
        self.escrever_nome(nome_user)
        self.escrever_senha(senha_user)
        self.submit()

class Credenciais(SauceDemoPage):
    usuarios = (By.ID, "login_credentials")
    senhas = (By.CLASS_NAME, "login_password")

    def get_usuarios(self):
        string = self.encontrar_elemento(self.usuarios).text
        # string = pagina.driver.find_element(By.ID, "login_credentials").text
        vetor = string.split('\n')[1:]
        return vetor
    
    def get_senhas(self):
        string = self.encontrar_elemento(self.senhas).text
        vetor = string.split('\n')[1:]
        return vetor

pagina = CaixaLogin()
credenciais = Credenciais()
pagina.entrar()

print(pagina.get_titulo())
print(credenciais.get_usuarios)

pagina.logar('standard_user', 'secret_sauce')


sleep(5)
