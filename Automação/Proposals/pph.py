from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException, TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import json
import pickle

caminho_chromedriver = r"C:\Users\Michele\Downloads\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=caminho_chromedriver)
driver = webdriver.Chrome(service=service)

driver.get("https://www.peopleperhour.com/freelance-jobs/technology-programming?experienceLevel=1%2C2")

cookies = pickle.load(open("cookies/pph_cookies.pkl", "rb"))

for cookie in cookies:
    if 'domain' in cookie:
        del cookie['domain']
    driver.add_cookie(cookie)

driver.refresh()


