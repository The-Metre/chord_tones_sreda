from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model, required for running in CI
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

browser = webdriver.Chrome()
browser.get('http://localhost:8000')     

body = browser.find_element(By.TAG_NAME, 'body')
page_text = body.text

assert 'Test view' in page_text