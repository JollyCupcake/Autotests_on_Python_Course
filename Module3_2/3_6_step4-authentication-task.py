import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import NoSuchElementException
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser after test")
    browser.quit()

@pytest.mark.parametrize('urls', ["https://stepik.org/lesson/236895/step/1",
                                   "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1",
                                   "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1",
                                   "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"
                                ])

class TestLoginSendAnswer():
    def test_open_link1(self, browser, urls):
        
        link = urls
        browser.get(link)
        browser.implicitly_wait(20)

        button = browser.find_element(By.CSS_SELECTOR, "a[href$=\"login\"]")
        browser.implicitly_wait(15)
        button.click()

        browser.implicitly_wait(15)
    
    # !DELETE INFO!
        input_login = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
        input_login.send_keys("XXXXXXXX@mail.ru")
        input_password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        input_password.send_keys("XXXXXXXX")

        button2 = browser.find_element(By.CSS_SELECTOR,"button.sign-form__btn")
        button2.click()

        time.sleep(15)
#---------------------------------

        input_answer = browser.find_element(By.TAG_NAME,"textarea")
        input_answer.send_keys(str(math.log(int(time.time()+ 0.2))))

            #wait = WebDriverWait(browser, 20)
            #button3 = wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR,"button.submit-submission"))
        button3 = browser.find_element(By.CLASS_NAME,"submit-submission")
        button3.click()
        time.sleep(20)
            #wait = WebDriverWait(browser, 30)
            #hint = wait.until(EC.visibility_of_element_located(By.CLASS_NAME,"smart-hints_hint"))
        hint = browser.find_element(By.CLASS_NAME,"smart-hints__hint")
        hint_answer = hint.text
        time.sleep(5)
            
            #assert hint_answer == "Correct!", "Wrong answer!"

        if hint.text != "Correct!":
                print(hint_answer)
                
        # browser.implicitly_wait(10)
        # button_again = browser.find_element(By.CSS_SELECTOR, "button.again-btn")
        # button_again.click()







        