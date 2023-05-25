from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then

driver = webdriver.Chrome()

@given(u'que eu esteja na tela de login do sistema')
def entrar_no_sistema(context):
    driver.get('https://www.saucedemo.com/')

@when(u'o usuário digita seu username')
def escrever_username(context):
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')

@when(u'digita sua senha')
def escrever_senha(context):
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')

@when(u'clica em submit')
def submit(context):
    driver.find_element(By.ID, 'login-button').click()

@then(u'o usuário deve estar logado')
def assert_login_sucesso(context):
    assert 'inventory' in driver.current_url