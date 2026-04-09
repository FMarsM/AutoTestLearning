from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/7/7.html")
a = browser.find_elements(By.TAG_NAME, "option")
res = 0
for c in a:
    if c.text.isdigit():
        res += int(c.text)
browser.find_element(By.ID, "input_result").send_keys(res)
browser.find_element(By.CLASS_NAME, "btn").click()
print(browser.find_element(By.ID, "result").text)
browser.quit()