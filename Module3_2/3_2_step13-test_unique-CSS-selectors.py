from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

# Inheriting from the TestCase class is the way to tell unittest module 
# that this is a test case:
class TestAbs(unittest.TestCase):
  
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_registration1(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element(By.CSS_SELECTOR, ".form-control.first[required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".form-control.second[required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.third[required]")
        input3.send_keys("Petxrov@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elem = browser.find_element(By.TAG_NAME, "h1")
        actual_welcome_text = welcome_text_elem.text
        expected_welcome_text = "Congratulations! You have successfully registered!"

    #с помощью self.assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual (actual_welcome_text, expected_welcome_text, "Registration unsuccessful")


    def test_registration2(self):
        browser = self.browser
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element(By.CSS_SELECTOR, ".form-control.first[required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".form-control.second[required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.third[required]")
        input3.send_keys("Petrov@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elem = browser.find_element(By.TAG_NAME, "h1")
        actual_welcome_text = welcome_text_elem.text
        expected_welcome_text = "Congratulations! You have successfully registered!"

    #с помощью self.assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual (actual_welcome_text, expected_welcome_text, "Registration unsuccessful")

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()