from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/methods/5/index.html")
links = browser.find_elements(By.TAG_NAME, "a")
hrefs = []
maxexp = 0
maxind = 0
i = 0
allc = []
for c in links:
    hrefs.append(c.get_attribute("href"))

for d in hrefs:
    browser.get(d)
    for c in browser.get_cookies():
        exp = c["expiry"]
    if exp >= maxexp:
        maxexp = exp
        maxind = i
    i += 1

browser.get(hrefs[maxind])
print(browser.find_element(By.ID, "result").text)
browser.quit()