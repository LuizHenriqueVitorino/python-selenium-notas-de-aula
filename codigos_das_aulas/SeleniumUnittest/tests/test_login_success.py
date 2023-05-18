
from pages.login_page import CaixaLoginPage, CredenciaisPage
from test_base import TestBase
from selenium.webdriver.common.by import By
import unittest

class TestLoginSuccess(TestBase):
    def test_login_success(self):
        self.login = CaixaLoginPage(self.driver)
        self.credenciais = CredenciaisPage(self.driver)

        self.login.entrar()
        usuario_sucesso = self.credenciais.get_usuarios()[0]
        senha = self.credenciais.get_senhas()[0]
        self.login.logar(usuario_sucesso, senha)
        
        self.assertIn('inventory', self.driver.current_url)

