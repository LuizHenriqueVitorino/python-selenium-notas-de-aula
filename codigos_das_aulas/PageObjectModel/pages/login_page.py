from pages.base_page import BasePage
from utils.locators import LoginLocatos

class CaixaLoginPage(BasePage):
    def __init__(self, driver) -> None:
        self.locator = LoginLocatos
        super(CaixaLoginPage, self).__init__(driver)
        
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

class CredenciaisPage(BasePage):
    def __init__(self, driver) -> None:
        self.locator = LoginLocatos
        super(CredenciaisPage, self).__init__(driver)

    def get_usuarios(self):
        string = self.encontrar_elemento(self.locator.USUARIOS).text
        # string = pagina.driver.find_element(By.ID, "login_credentials").text
        vetor = string.split('\n')[1:]
        return vetor
    
    def get_senhas(self):
        string = self.encontrar_elemento(self.locator.SENHAS).text
        vetor = string.split('\n')[1:]
        return vetor