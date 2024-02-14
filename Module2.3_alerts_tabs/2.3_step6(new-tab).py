from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()

    #switching to the second tab (the count starts with 0, so we are switching to [1] in our code)
    browser.switch_to.window(browser.window_handles[1])


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    #рассчитываем y по формуле
    def calc(x): 
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)

    #вставляем в input1 значение рассчитанной переменной y
    browser.find_element(By.ID, "answer").send_keys(y)


    # отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button").click()


   

finally:
    
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла