from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/6/6.3.1/index.html")
print(browser.get_cookie("token_22")["value"])
time.sleep(3)
browser.quit()