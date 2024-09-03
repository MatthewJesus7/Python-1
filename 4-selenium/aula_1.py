from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Caminho para o chromedriver
service = Service(executable_path='C:/Users/Michele/chromedriver')

# Inicialize o WebDriver com o serviço
driver = webdriver.Chrome(service=service)

# Continue com o resto do seu código

# Acesse uma página
driver.get("http://www.google.com")

# Imprima o título da página
print(driver.title)

# Feche o navegador
driver.quit()