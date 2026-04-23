from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/methods/3/index.html")
cookies = browser.get_cookies()
res = 0
for c in cookies:
    if "secret_cookie" in c["name"]:
        res += int(c["value"])

print(res)

browser.quit()