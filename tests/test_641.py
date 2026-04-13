from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/6/6.3.3/index.html")
browser.add_cookie({"name": "secretKey", "value": "selenium123"})
browser.refresh()
print(browser.find_element(By.ID, "password").text)
browser.quit()