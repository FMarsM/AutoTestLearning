from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/7/7.3.3/index.html")
actions = ActionChains(browser)
actions.key_down(Keys.CONTROL).key_down(Keys.ALT).key_down(Keys.SHIFT).key_down("t").perform()
print(browser.find_element(By.XPATH, '//*[@key="access_code"]').text)
actions.key_up(Keys.CONTROL).key_up(Keys.ALT).key_up(Keys.SHIFT).key_up("t").perform()
browser.quit()