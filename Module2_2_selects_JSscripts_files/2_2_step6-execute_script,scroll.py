from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим элемент, в аттрибуте которого будем искать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    #рассчитываем y по формуле
    def calc(x): 
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    #вставляем в input1 значение рассчитанной переменной y
    browser.find_element(By.ID, "answer").send_keys(y)

    #скроллим страницу, пока button не станет видно
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    #отмечаем чекбокс I'm the robot
    browser.find_element(By.ID, "robotCheckbox").click()


    #выбираем радиокнопку Robots rule
    browser.find_element(By.ID, "robotsRule").click()

    
    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button").click()


    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
