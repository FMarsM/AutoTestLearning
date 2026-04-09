# Импорт модуля webdriver из библиотеки Selenium для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By

# Импорт модуля time для работы с задержками
import time

# Создание экземпляра webdriver браузера Chrome
browser = webdriver.Chrome()

# Открытие сайта "stepik.org" в браузере
browser.get("https://parsinger.ru/selenium/3/3.2.2/index.html")
browser.find_element(By.ID, "codeInput").send_keys("Дрогон")
browser.find_element(By.ID, "clickButton").click()

# Пауза на 5 секунд, чтобы страница успела загрузиться
time.sleep(5)

# Закрытие браузера
browser.quit()