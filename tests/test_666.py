from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/scroll/4/index.html")
btns = browser.find_elements(By.CLASS_NAME, "btn")
res = 0
for btn in btns:
    browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
    btn.click()
    res += int(browser.find_element(By.ID, "result").text)
print(res)
browser.quit()
