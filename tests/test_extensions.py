import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()

options_chrome.add_extension('C:\\autotests\\AutoTestLearning\\1.0.0_0.crx')




with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(15)
    a = browser.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))