import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
    Atividade da Letícia. Aprovado. Parabéns.
"""

class GitPage(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.wdw = WebDriverWait(self.browser, 10)
        self.browser.maximize_window()
        self.browser.get('https://github.com/LuizHenriqueVitorino')
    
    def test_open_repository(self):
        self.wdw.until(EC.presence_of_element_located((By.XPATH,"//div/nav/a[@data-tab-item='repositories']")))
        self.browser.find_element(By.XPATH,"//div/nav/a[@data-tab-item='repositories']").click()

        self.wdw.until(EC.presence_of_element_located((By.XPATH,'//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a')))
        self.browser.find_element(By.XPATH,'//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a').click()

        self.wdw.until(EC.presence_of_element_located((By.XPATH,'//*[@id="repository-container-header"]/div[1]/div[1]/div/strong/a')))
        element_text = self.browser.find_element(By.XPATH,'//*[@id="repository-container-header"]/div[1]/div[1]/div/strong/a').text
        self.browser.save_screenshot('codigos_das_aulas/Unittest/screenshots/tela.png')
        self.assertIn('python-selenium-notas-de-aula',element_text)


    def tearDown(self):
        self.browser.close()
        
if __name__ == "__main__":     
    unittest.main()