from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

def login(username, password):
    browser.get("http://127.0.0.1:8000/todo")
    user = browser.find_element_by_name("username").send_keys(username)
    passwrd = browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_xpath("//input[@value='login']").click()

def DisplayListofArchivedItems():
    browser.get("http://127.0.0.1:8000/todohist/")
    #returns the name in ul tag which is "List of Archived Items"
    return browser.find_element_by_xpath("//ul").get_attribute("name")


browser = webdriver.Chrome()
login("myusername", "mypassword")
DisplayListofArchivedItems()
# browser.close()
