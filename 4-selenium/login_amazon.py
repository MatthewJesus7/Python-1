from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pickle
import time

# Caminho do chromedriver
caminho_chromedriver = r"C:\Users\Michele\Downloads\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=caminho_chromedriver)

# Inicia o webdriver
driver = webdriver.Chrome(service=service)

# URL de login da Amazon
driver.get('https://www.amazon.com')

# Aqui você deve fazer login manualmente na Amazon (uma vez)
time.sleep(600)  # Espera até que você faça login manualmente (ajuste o tempo se necessário)

# Salvar os cookies depois de logar manualmente
pickle.dump(driver.get_cookies(), open("amazon_cookies.pkl", "wb"))

# Fechar o navegador
driver.quit()
