from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/6/6.5/index.html")
browser.execute_script("return arguments[0].scrollIntoView(true);", browser.find_element(By.ID, "target"))
browser.find_element(By.ID, "target").click()
print(browser.find_element(By.ID, "secret-key").text)
time.sleep(10)
browser.quit()