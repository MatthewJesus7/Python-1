from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import time

caminho_chromedriver = r"C:\Users\Michele\Downloads\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=caminho_chromedriver)

driver = webdriver.Chrome(service=service)

# Acessa o site inicial
driver.get("https://www.tudocelular.com/celulares/fichas-tecnicas.html?o=2")


elementos_links = driver.find_elements(By.CSS_SELECTOR, ".pic")

urls = [element.get_attribute("href") for element in elementos_links]

# Abrindo a primeira URL na guia atual
driver.get(urls[0])

# Opcional: Espera alguns segundos para carregar as páginas
# time.sleep(0)

all_texts = []

all_texts.append(driver.find_element(By.TAG_NAME, "body").text)  # Extrai e armazena o texto

# Abrindo cada URL em uma nova guia e extraindo o texto
for url in urls[1:]:
    driver.execute_script("window.open('');")  # Abre uma nova guia
    driver.switch_to.window(driver.window_handles[-1])  # Muda para a nova guia
    driver.get(url)  # Acessa a URL
    page_text = driver.find_element(By.TAG_NAME, "body").text  # Extrai o texto da página
    all_texts.append(page_text)  # Armazena o texto extraído

# Agora 'all_texts' contém o texto de todas as páginas
for index, text in enumerate(all_texts):
    print(f"Texto da página {index + 1}:")
    print(text)
    print("\n" + "-" * 50 + "\n")
