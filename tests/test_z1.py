from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/1/1.html")
a = browser.find_elements(By.CLASS_NAME, "form")
for c in a:
    c.send_keys("Текст")
browser.find_element(By.ID, "btn").click()
print(browser.find_element(By.ID, "result").text)
browser.quit()