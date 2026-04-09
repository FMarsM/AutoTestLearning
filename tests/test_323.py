# Импорт модуля webdriver из библиотеки Selenium для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By

# Импорт модуля time для работы с задержками
import time

from selenium.webdriver.common.keys import Keys

# Создание экземпляра webdriver браузера Chrome
browser = webdriver.Chrome()

# Открытие сайта "stepik.org" в браузере
browser.get("https://parsinger.ru/selenium/3/3.3.3/index.html")
a = browser.find_elements(By.TAG_NAME, "a")
res = 0
for c in a:
    n = c.get_attribute("stormtrooper")
    if n.isdigit():
        res += int(n)
browser.find_element(By.ID, "inputNumber").send_keys(str(res))
browser.find_element(By.ID, "checkBtn").click()
print(res)


# Пауза на 5 секунд, чтобы страница успела загрузиться
time.sleep(5)

# Закрытие браузера
browser.quit()