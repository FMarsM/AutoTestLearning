from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/3/3.3.1/index.html")
a = browser.find_element(By.ID, "parent_id").find_element(By.CLASS_NAME, "child_class")
a.click()
print(a.get_attribute("password"))
browser.quit()