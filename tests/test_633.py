from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/6/6.3.2/index.html")
browser.delete_all_cookies()
time.sleep(5)
print(browser.find_element(By.ID, "password").text)
time.sleep(5)
browser.quit()