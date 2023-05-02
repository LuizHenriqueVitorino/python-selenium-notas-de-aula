from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial
from time import sleep


class Funcoes :
    def __init__(self, url: str) -> None:
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def wait_element(self, by: By, element: str, webdriver):
        elements = webdriver.find_elements(by, element)
        print('O elemento está aí?')
        return bool(elements)

    def clicar_no_botao(self, id_botao: str):
        wait_button = partial(self.wait_element, By.ID, id_botao)
        self.wait.until(wait_button, "O botão foi pra Narnia!")
        button = self.driver.find_element(By.ID, id_botao)
        button.click()
        sleep(10)

    def entrar_na_aplicacao(self, url): 
        self.driver.get(url)
