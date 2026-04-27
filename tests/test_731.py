from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/7/7.3.1/index.html")
drag = browser.find_element(By.ID, "draggable")
target = browser.find_element(By.ID, "target")
actions = ActionChains(browser)
actions.drag_and_drop(drag,target).perform()
print(browser.find_element(By.ID, "password").text)
browser.quit()
