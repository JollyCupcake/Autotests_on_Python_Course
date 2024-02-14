from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #считываем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text


    #рассчитываем y по формуле
    def calc(x): 
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    #вставляем в input1 значение рассчитанной переменной y
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    #отмечаем чекбокс I'm the robot
    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    #выбираем радиокнопку Robots rule
    radiobutton1 = browser.find_element(By.ID, "robotsRule")
    radiobutton1.click()

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
