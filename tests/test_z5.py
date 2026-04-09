from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/4/4.html")
a = browser.find_elements(By.CLASS_NAME, "check")
for c in a:
    c.click()
browser.find_element(By.CLASS_NAME, "btn").click()
time.sleep(15)
print(browser.find_element(By.ID, "result").text)
browser.quit()