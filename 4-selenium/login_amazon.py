import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

caminho_chromedriver = r"C:\Users\Michele\Downloads\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=caminho_chromedriver)

driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com")

print("Faça login manualmente na Amazon...")

input("Depois de fazer login manualmente, pressione Enter para continuar...")

cookies = driver.get_cookies()
pickle.dump(cookies, open("amazon_cookies.pkl", "wb"))
print("Cookies salvos com sucesso.")

