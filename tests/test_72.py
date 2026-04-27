from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/7/7.2/index.html")
past = []
while len(past) != 100:
    elements = browser.find_elements(By.CLASS_NAME, "interactive")
    for el in elements:
        if el not in past:
            past.append(el)
            el.send_keys("1")
            el.send_keys(Keys.ENTER)
            el.send_keys(Keys.ARROW_DOWN)
print(browser.find_element(By.ID, "hidden-password").text)
time.sleep(5)
browser.quit()