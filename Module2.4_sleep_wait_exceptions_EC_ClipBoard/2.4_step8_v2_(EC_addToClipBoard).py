from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
import pyperclip


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Wait for the element with ID "price" to contain the text "$100"
price_element = WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element ((By.ID, "price"), "$100")
)

button = browser.find_element(By.ID, "book")
button.click()


x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
    
# def calc(x): 
#    return str(math.log(abs(12*math.sin(int(x)))))
# y = calc(x)
# browser.find_element(By.ID, "answer").send_keys(y)

browser.find_element(By.ID, "answer").send_keys(
  str(math.log(abs(12*math.sin(int(browser.find_element(By.ID, "input_value").text)))))
)

# отправляем заполненную форму
button2 = browser.find_element(By.ID, "solve")
button2.click()

alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)


time.sleep(10)
browser.quit()