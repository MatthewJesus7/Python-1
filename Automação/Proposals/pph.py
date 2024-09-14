from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pickle

# Caminho para o chromedriver
caminho_chromedriver = r"C:\Users\Michele\Downloads\chromedriver-win64\chromedriver.exe"

# Iniciar o serviço do ChromeDriver
service = Service(executable_path=caminho_chromedriver)
driver = webdriver.Chrome(service=service)

# Acessa o site
driver.get("https://www.peopleperhour.com/freelance-jobs/technology-programming?experienceLevel=1%2C2")

# &page=2

# Carrega os cookies
cookies = pickle.load(open("cookies/pph_cookies.pkl", "rb"))
for cookie in cookies:
    if 'domain' in cookie:
        del cookie['domain']
    driver.add_cookie(cookie)

# Atualiza a página com os cookies
driver.refresh()

# Define os seletores corretos para as propostas
painel_de_propostas = driver.find_elements(By.CLASS_NAME, "list⤍List⤚3R-r9")

links_das_propostas = driver.find_elements(By.CLASS_NAME, "item__url⤍ListItem⤚20ULx")
urls = [link_da_proposta.get_attribute("href") for link_da_proposta in links_das_propostas]

propostas = []

try:
    # Extrai o texto de cada proposta
    for proposta in painel_de_propostas:
        propostas.append(proposta.text)

except Exception as e:
    print(f"Erro ao obter as propostas: {e}")

print(propostas, urls)

driver.quit()