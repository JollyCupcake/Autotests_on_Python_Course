from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим элемент, в аттрибуте которого будем искать значение для переменной x
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")


    #рассчитываем y по формуле
    def calc(x): 
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    #вставляем в input1 значение рассчитанной переменной y
    browser.find_element(By.ID, "answer").send_keys(y)


    #отмечаем чекбокс I'm the robot
    browser.find_element(By.ID, "robotCheckbox").click()


    #выбираем радиокнопку Robots rule
    browser.find_element(By.ID, "robotsRule").click()


    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
