from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/6/6.2/index.html")
time.sleep(5)
browser.find_element(By.TAG_NAME, "a").click()
time.sleep(5)
browser.find_element(By.TAG_NAME, "a").click()
time.sleep(5)
browser.back()
time.sleep(5)
browser.back()
time.sleep(5)
print(browser.find_element(By.ID, "getPasswordBtn").click())
time.sleep(15)
browser.quit()