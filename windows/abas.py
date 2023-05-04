from selenium import webdriver
from time import sleep

"""
    NOTAS DE AULA:
    janelas = abas (para o navegador)
    janelas são identificadas por ids
    current_window_handle -> retorna uma string do ai da janela atual
    window_handles -> retorna uma lista com os ids de todas as janelas abertas
"""

driver = webdriver.Chrome()
driver.get('https://github.com/LuizHenriqueVitorino/python-selenium-notas-de-aula')
driver.switch_to.new_window('tab')
driver.get('https://luizhenriquevitorino.github.io/Curriculo/html/')
driver.switch_to.new_window('tab')
driver.get('https://web.whatsapp.com/')

driver.current_url

def encontra_janela(palavra: str) -> bool:
    windows = driver.window_handles # Retorna uma lista de IDs
    for win in windows:
        driver.switch_to.window(win)
        if palavra in driver.current_url:
            print(f'Encontrei a janela {driver.current_url}')
            return True
    print(f'Não encontrei nenuma janela com a palavra: {palavra}')
    return False


encontra_janela('Curriculo')

sleep(10)

driver.quit()