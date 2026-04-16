from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/5.5/2/1.html")

for c in browser.find_elements(By.CLASS_NAME, "text-field"):
    if not c.get_attribute("disabled"):
        c.clear()
browser.find_element(By.ID, "checkButton").click()
print(browser.switch_to.alert.text)
browser.quit()