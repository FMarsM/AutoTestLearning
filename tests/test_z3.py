from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/3/3.html")
a = browser.find_elements(By.TAG_NAME, "p")
res = 0
for c in a:
    if c.text.isdigit():
        res += int(c.text)
print(res)
browser.quit()