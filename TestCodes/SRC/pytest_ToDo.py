from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

def DisplayListofItems():
    browser.get("http://127.0.0.1:8000/todo/")
    return browser.find_element_by_xpath("//ul").get_attribute("name")


browser = webdriver.Chrome()
DisplayListofItems()
browser.close()
