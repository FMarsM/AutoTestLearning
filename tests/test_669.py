from selenium import webdriver
from selenium.webdriver.common.bidi import browser
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://parsinger.ru/selenium/5.5/5/1.html")
divs = browser.find_elements(By.XPATH, '//*[@id="main-container"]/div[contains(style, "")]')
for div in divs:
    stext = div.find_element(By.TAG_NAME, "span").text
    select = div.find_element(By.TAG_NAME, "select")
    select.click()
    select.find_element(By.XPATH, f'.//*[@value="{stext}"]').click()
    div.find_element(By.XPATH, f'.//*[@data-hex="{stext}"]').click()
    div.find_element(By.XPATH, f'.//*[@type="checkbox"]').click()
    div.find_element(By.XPATH, f'.//*[@type="text"]').send_keys(stext)
    div.find_element(By.XPATH, f'.//button[contains(text(), "Проверить")]').click()
browser.find_element(By.XPATH, f'.//button[contains(text(), "Проверить")]').click()
time.sleep(5)
browser.quit()