from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/7/7.1/index.html")
height = browser.execute_script("return document.body.scrollHeight")
browser.execute_script(f"window.scrollBy(0,{height})")
time.sleep(1)
print(browser.find_element(By.ID, "secret-container").text)
browser.quit()