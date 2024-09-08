from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

caminho_chromedriver = r"C:\Users\Michele\Downloads\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=caminho_chromedriver)
driver = webdriver.Chrome(service=service)

driver.get("https://www.tudocelular.com/celulares/fichas-tecnicas.html?o=2")
elementos_links = driver.find_elements(By.CSS_SELECTOR, ".pic")
urls = [element.get_attribute("href") for element in elementos_links]

cards = []  # Lista para armazenar todos os dados coletados

for index, url in enumerate(urls):
    driver.execute_script("window.open('');") 
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    
    try:
        itens_compra = driver.find_elements(By.CLASS_NAME, "item_compra")
        
        for item in itens_compra:
            try:
                shop_logo_div = item.find_element(By.CLASS_NAME, "shop_logo")
                img_element = shop_logo_div.find_element(By.TAG_NAME, "img")
                loja_nome = img_element.get_attribute("alt")
                
                if "Amazon" in loja_nome:
                    print(f"'Amazon' encontrado na página {index + 1}. Abrindo oferta da Amazon.")

                    oferta_link = item.find_element(By.CSS_SELECTOR, ".green_button").get_attribute("href")
                    
                    driver.execute_script(f"window.open('{oferta_link}');")
                    driver.switch_to.window(driver.window_handles[-1]) 
                    
                    # Aguardar que a nova página da Amazon seja carregada
                    WebDriverWait(driver, 20).until(EC.url_contains("amazon"))
                    driver.get(driver.current_url)  # Certifique-se de que a URL foi carregada completamente
                    
                    try:
                        # Extração de dados da página da Amazon com tempos de espera maiores
                        titles = WebDriverWait(driver, 20).until(
                            EC.presence_of_all_elements_located((By.ID, 'productTitle'))
                        )
                        prices = WebDriverWait(driver, 20).until(
                            EC.presence_of_all_elements_located((By.CLASS_NAME, 'best-offer-name'))
                        )
                        total_prices = WebDriverWait(driver, 20).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.a-offscreen'))
                        )

                        # Verificar se o número de elementos extraídos é o mesmo
                        num_items = min(len(titles), len(prices), len(total_prices))

                        # Armazenar os dados em uma lista de cartões
                        for i in range(num_items):
                            title = titles[i].text
                            price = prices[i].text
                            total_price = total_prices[i].text
                            
                            # Adicionar os dados como um dicionário à lista 'cards'
                            cards.append({'title': title, 'price': price, 'total_price': total_price})

                        print(f"Dados coletados da página {index + 1}: {cards}")
                        
                    except TimeoutException:
                        print(f"Timeout ao carregar elementos na página da Amazon (página {index + 1}).")
                    
                    break  # Sair do loop quando encontrar a oferta da Amazon
                    
            except NoSuchElementException:
                print(f"Elemento não encontrado em um item na página {index + 1}, pulando item...")
    
    except Exception as e:
        print(f"Erro na página {index + 1}: {e}")

    driver.close()
    driver.switch_to.window(driver.window_handles[-1])

# Passo 5: Salvar todos os dados coletados em um arquivo CSV
if cards:
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price', 'total_price'])
        writer.writeheader()  # Escreve os cabeçalhos do CSV
        writer.writerows(cards)  # Escreve os dados no CSV
    print(f"Dados salvos no arquivo CSV: {cards}")
else:
    print("Nenhum dado foi coletado.")

driver.quit()
