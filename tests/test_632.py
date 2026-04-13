from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/6/6.3/index.html")
a = browser.get_cookies()
for c in a:
    browser.find_element(By.ID, "phraseInput").send_keys(c["name"])
browser.find_element(By.ID, "checkButton").click()
time.sleep(3)
print(browser.find_element(By.ID, "result").text)
browser.quit()