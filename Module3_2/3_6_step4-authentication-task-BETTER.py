import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser after test")
    browser.quit()

@pytest.mark.parametrize('urls', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])

class TestAliens():
    def test_open_link1(self, browser, urls):
        link = f"https://stepik.org/lesson/{urls}/step/1"
        browser.get(link)
        browser.implicitly_wait(20)

        button = browser.find_element(By.CSS_SELECTOR, "a[href$=\"login\"]")
        browser.implicitly_wait(15)
        button.click()
        browser.implicitly_wait(15)
    
    #-----------!SENSITIVE INFO!----------
        browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys("XXX@mail.ru")
        browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys("XXX")
        browser.find_element(By.CSS_SELECTOR,"button.sign-form__btn").click()
        time.sleep(15)
    #-----------!SENSITIVE INFO!--------

        browser.find_element(By.TAG_NAME,"textarea").send_keys(str(math.log(int(time.time()+ 0.2))))
        browser.find_element(By.CLASS_NAME,"submit-submission").click()
        time.sleep(20)

        hint = browser.find_element(By.CLASS_NAME,"smart-hints__hint").text
        time.sleep(5)

        if hint != "Correct!":
                print(hint)
                
                







        