from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pickle
import time

caminho_chromedriver = r"C:\Users\Michele\Downloads\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=caminho_chromedriver)

driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com')

time.sleep(120)

pickle.dump(driver.get_cookies(), open("amazon_cookies.pkl", "wb"))

driver.quit()
