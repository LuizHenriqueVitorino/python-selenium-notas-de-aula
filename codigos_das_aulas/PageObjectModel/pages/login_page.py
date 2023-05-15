from pages.base_page import BasePage
from utils.locators import LoginLocatos

class CaixaLogin(BasePage):
    def __init__(self, driver) -> None:
        self.locator = LoginLocatos
        super(CaixaLogin, self).__init__(driver)
        
    def escrever_nome(self, nome_str: str):
        self.escrever(self.locator.NOME, nome_str)

    def escrever_senha(self, senha_str: str):
        self.escrever(self.locator.SENHA, senha_str)
    
    def submit(self):
        self.clicar(self.locator.BOTAO)

    def logar(self, nome_user, senha_user):
        self.escrever_nome(nome_user)
        self.escrever_senha(senha_user)
        self.submit()