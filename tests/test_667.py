from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/5.5/3/1.html")
parents = browser.find_elements(By.CLASS_NAME, "parent")
res = 0
for p in parents:
    if p.find_element(By.CLASS_NAME, "checkbox").is_selected():
        res += int(p.find_element(By.TAG_NAME, "textarea").get_attribute("value"))
print(res)

browser.quit()
