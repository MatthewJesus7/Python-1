from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pickle

caminho_chromedriver = r"C:\Users\Michele\Downloads\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=caminho_chromedriver)
driver = webdriver.Chrome(service=service)

driver.get("https://www.peopleperhour.com/freelance-jobs/technology-programming?experienceLevel=1%2C2")

input("Depois de fazer login manualmente, pressione Enter para continuar...")

cookies = driver.get_cookies()
pickle.dump(cookies, open("pph_cookies.pkl", "wb"))
print("Cookies salvos com sucesso.")