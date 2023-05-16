import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

"""
    OBS: Nossa intenção com o unittest é rodar uma suite de testes
"""

class GitHubTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://github.com/LuizHenriqueVitorino")

    def test_gitHub(self):
        nome = self.driver.find_element(By.CLASS_NAME, "p-name").text
        self.assertIn("Henrique", nome)
    
    def test_linkedin(self):
        linkedin_btn = self.driver.find_element(By.XPATH, '//*[@id="user-profile-frame"]/div/div[1]/div/article/div[3]/a[1]')
        linkedin_btn.click()
        self.assertIn("linkedin", self.driver.current_url)

    def tearDown(self):
        sleep(5)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    