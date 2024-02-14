from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим число 1
    num1 = browser.find_element(By.ID, "num1")
    x = num1.text
    int_x = int(x)

    #находим число 2
    num2 = browser.find_element(By.ID, "num2")
    y = num2.text
    int_y = int(y)

    #рассчитываем z сумму чисел 1 и 2
    int_z = int_x+int_y
    
    #конвертируем int_z в string
    z = str(int_z)

    #ищем элемент select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value=(z))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
