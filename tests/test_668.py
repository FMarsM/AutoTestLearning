from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/5.5/4/1.html")
parents = browser.find_elements(By.CLASS_NAME, "parent")
for p in parents:
        gray = p.find_element(By.CSS_SELECTOR, f":nth-child(1)")
        blue = p.find_element(By.CSS_SELECTOR, f":nth-child(2)")
        blue.send_keys(gray.text)
        gray.clear()
        p.find_element(By.TAG_NAME, "button").click()
browser.find_element(By.ID, "checkAll").click()
time.sleep(15)
browser.quit()
