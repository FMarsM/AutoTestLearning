from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/6/6.2.1/index.html")
browser.find_element(By.ID, "this_pic").screenshot("file.jpg")
time.sleep(15)
browser.quit()