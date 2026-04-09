from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/2/2.html")
browser.find_element(By.PARTIAL_LINK_TEXT, "16243162441624").click()
print(browser.find_element(By.ID, "result").text)
browser.quit()