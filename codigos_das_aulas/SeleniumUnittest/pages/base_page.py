from abc import ABC

class BasePage(ABC):
    def __init__(self, driver) -> None:
        self.driver = driver
        self.url = 'https://www.saucedemo.com/'

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)
    
    def escrever(self, locator, str):
        self.encontrar_elemento(locator).send_keys(str)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def entrar(self) -> None:
        self.driver.get(self.url)