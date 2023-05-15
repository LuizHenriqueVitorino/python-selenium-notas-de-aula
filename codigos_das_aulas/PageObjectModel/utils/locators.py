from selenium.webdriver.common.by import By

class LoginLocatos:
    NOME = (By.ID, "user-name")
    SENHA = (By.ID, "password")
    BOTAO = (By.ID, "login-button")
    USUARIOS = (By.ID, "login_credentials")
    SENHAS = (By.CLASS_NAME, "login_password")