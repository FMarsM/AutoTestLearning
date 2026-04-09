from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/6/6.html")
a = browser.find_elements(By.CLASS_NAME, "num")
res = browser.find_element(By.ID, "text_box").text
res1 = eval(res)
print(res1)
browser.find_element(By.ID, "selectId").click()
opts = browser.find_elements(By.TAG_NAME, "option")
for c in opts:
    if int(c.text) == int(res1):
        c.click()
browser.find_element(By.CLASS_NAME, "btn").click()
time.sleep(10)
browser.quit()