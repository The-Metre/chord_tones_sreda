from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('http://localhost:8000')     

body = browser.find_element(By.TAG_NAME, 'body')
page_text = body.text

assert 'Test view' in page_text