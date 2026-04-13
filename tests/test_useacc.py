import time
from selenium import webdriver

# Задаем опции для Chrome
options_chrome = webdriver.ChromeOptions()

# Указываем путь к User Data (БЕЗ \Default в конце!)
options_chrome.add_argument('--user-data-dir=C:\\Users\\Марсель\\AppData\\Local\\Google\\Chrome\\User Data')

# Указываем конкретный профиль
options_chrome.add_argument('--profile-directory=Default')

# Инициализируем драйвер с указанными опциями
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)  # Открываем страницу
    time.sleep(10)  # Даем время на загрузку страницы
