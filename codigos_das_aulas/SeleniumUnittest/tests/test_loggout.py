from pages.login_page import CaixaLoginPage, CredenciaisPage
from test_base import TestBase

class TestLoggoutSuccess(TestBase):
    def test_loggout_success(self):
        self.login = CaixaLoginPage(self.driver)
        self.credenciais = CredenciaisPage(self.driver)

        self.login.entrar()
        usuario_sucesso = self.credenciais.get_usuarios()[0]
        senha = self.credenciais.get_senhas()[0]
        self.login.logar(usuario_sucesso, senha)

        self.assertIn('Swag', self.driver.title)

