from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/7/7.3.5/index.html")
actions = ActionChains(browser)
time.sleep(1)
actions.click(browser.find_element(By.ID, "scrollable-container-left")).send_keys(Keys.END).perform()
actions.click(browser.find_element(By.ID, "scrollable-container-right")).send_keys(Keys.END).perform()
time.sleep(1)
print("\n" + browser.find_element(By.TAG_NAME, "span").text)
browser.quit()