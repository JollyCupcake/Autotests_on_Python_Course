import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button_found(browser):
    browser.get(link)
    
    assert browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"), "basket button not found"



