from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class SeleniumPage:
    def __init__(self) -> None:
        self.webdriver = webdriver.Chrome()

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

class SauceDemoPage(SeleniumPage):
    def __init__(self) -> None:
        super().__init__()
        self.driver = self.webdriver
        self.url = 'https://www.saucedemo.com/'

    def entrar(self) -> None:
        self.driver.get(self.url)

    def get_titulo(self):
        return self.driver.find_element(By.CLASS_NAME, "login_logo").text
    
    def escrever(self, locator, str):
        self.encontrar_elemento(locator).send_keys(str)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()
    
class CaixaLogin(SauceDemoPage):
    def __init__(self) -> None:
        super().__init__()
        self.nome = (By.ID, "user-name")
        self.senha = (By.ID, "password")
        self.botao = (By.ID, "login-button")

    def escrever_nome(self, nome_str: str):
        self.escrever(self.nome, nome_str)

    def escrever_senha(self, senha_str: str):
        self.escrever(self.senha, senha_str)
    
    def submit(self):
        self.clicar(self.botao)

pagina = CaixaLogin()
pagina.entrar()

pagina.escrever_nome("standard_user")
pagina.escrever_senha("secret_sauce")
pagina.submit()


sleep(5)
