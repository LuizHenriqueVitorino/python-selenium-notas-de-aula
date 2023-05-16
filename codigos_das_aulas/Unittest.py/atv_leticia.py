import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

"""
    Atividade da Letícia. Aprovado. Parabéns.
"""

class GitPage(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get('https://github.com/LuizHenriqueVitorino')
    
    def test_open_repository(self):
        sleep(5)
        self.browser.find_element(By.XPATH,"//div/nav/a[@data-tab-item='repositories']").click()
        sleep(5)
        self.browser.find_element(By.XPATH,'//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a').click()
        sleep(5)
        element_text = self.browser.find_element(By.XPATH,'//*[@id="repository-container-header"]/div[1]/div[1]/div/strong/a').text
        self.assertIn('python-selenium-notas-de-aula',element_text)
        self.browser.save_screenshot('screenShot/tela.png')

    def tearDown(self):
        self.browser.close()
        
        
if __name__ == "__main__":
    unittest.main()