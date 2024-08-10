# https://pypi.org/project/selenium/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome()
URL = "https://halykmarket.kz/category/televizori-i-audiotehnika"


element = WebDriverWait(browser, 20).until(
    ec.presence_of_element_located((By.TAG_NAME, "html"))
)
browser.get(URL)

assert 'Купить' in browser.title

products = browser.find_elements(By.CLASS_NAME, 'product-card-content')

titles = []
prices = []

for elem in products:
    titles.append(elem.find_element(By.CLASS_NAME, 'product-card-title').text)
    prices.append(elem.find_element(By.CLASS_NAME, 'product-card-value-value').text)
    
for title, price in zip(titles, prices):
    print(f"{title}: {price} тенге")

browser.quit()