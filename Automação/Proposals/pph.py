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
propostas = []

try:
    # Extrai o texto de cada proposta
    for proposta in painel_de_propostas:
        propostas.append(proposta.text)

except Exception as e:
    print(f"Erro ao obter as propostas: {e}")

# Suas habilidades e habilidades que você não possui
my_skills = [
    'frontend',
    'html',
    'css',
    'javascript',
    'react',
    'firebase',
    'python',
    'git',
    'github',
    'selenium',
    'web scraping',
    'website'
    'automation',             
    'integration',            
    'user experience',
    'frontend',
    'website design',  
]
not_my_skills = [
    'django',
    'shopify', 
    'email template design',
    'google analytics',
    'clay ai',
    'crm system',
    'zoho lead management',
    'google merchant',
    'wordpress',
    'excel',
    'data visualization',     
    'seo optimization'
]

# Função para pontuar as propostas
def pontuar_proposta(proposta):
    pontos = 0
    # Verifica as habilidades que você tem
    for skill in my_skills:
        if skill.lower() in proposta.lower():
            pontos += 1

    # Verifica as habilidades que você não tem e subtrai pontos
    for skill in not_my_skills:
        if skill.lower() in proposta.lower():
            pontos -= 1

    return pontos

# Pontua as propostas
propostas_com_pontos = []
for proposta in propostas:
    pontos = pontuar_proposta(proposta)
    propostas_com_pontos.append((proposta, pontos))

# Ordena as propostas por pontuação (maior para menor)
propostas_com_pontos.sort(key=lambda x: x[1], reverse=True)

print("Propostas classificadas por pontuação (maior para menor):")
for proposta, pontos in propostas_com_pontos:
    print(f"Pontuação: {pontos} - Proposta: {proposta}")
    
driver.quit()
