from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/7/7.3.2/index.html")
btn = browser.find_element(By.ID, "dblclick-area")
actions = ActionChains(browser)
actions.double_click(btn).perform()
print(browser.find_element(By.ID, "password").text)
browser.quit()