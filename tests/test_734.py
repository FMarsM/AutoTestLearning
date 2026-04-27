from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/7/7.3.4/index.html")
actions = ActionChains(browser)
actions.context_click(browser.find_element(By.ID, "context-area")).perform()
browser.find_element(By.XPATH, '//*[@data-action="get_password"]').click()
print()
print(browser.find_element(By.XPATH, '//*[@key="access_code"]').text)
browser.quit()