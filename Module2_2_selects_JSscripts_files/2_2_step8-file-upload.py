from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("petrov@gmail.com")
    
    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname("m2_les2_step8.py")) 
    file_name = "fileforstep8.txt"      # задаём переменную для файла, который будем загружать на сайт
    file_path = os.path.join(current_dir, file_name)  # получаем путь к файлу fileforstep8.txt
    
    # ищем элемент для загрузки файла
    choosefile_element = browser.find_element(By.CSS_SELECTOR, "[type='file']")

    # отправляем файл
    choosefile_element.send_keys(file_path)

    # отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button").click()

   

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла