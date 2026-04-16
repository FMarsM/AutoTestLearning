from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/methods/1/index.html")
while not browser.find_element(By.ID, "result").text.isdigit():
    browser.refresh()
print(browser.find_element(By.ID, "result").text)
browser.quit()