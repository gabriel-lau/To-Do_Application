import pytest
from SRC.pytest_ToDo import *
import re

# Functions
def addItems(string):
    input = browser.find_element_by_name("content")
    input.send_keys(string)
    input.send_keys(Keys.RETURN)
    return True

def login(username, password):
    browser.get("http://127.0.0.1:8000/todo")
    user = browser.find_element_by_name("username").send_keys(username)
    passwrd = browser.find_element_by_name("password").send_keys(password)
    browser.find_element_by_xpath("//input[@value='Login']").click()

#Test Cases

##SPRINT 1
# def test_DisplayListOfItems():
#     assert "List of Items"
#
# def test_AddBlankItem():
#     browser.find_element_by_xpath("//input[@value='Add']").click()
#     popup = browser.switch_to.alert
#     message= popup.text
#     assert message == "Text field must be filled"
#     popup.accept()
#
# def test_AddValidItem():
#     addItems("to be deleted")
#     addItems("jd's test item")
#     assert "jd's test item" in browser.page_source
#
# def test_AddExistingItem():
#     addItems("jd's test item")
#     page = browser.page_source
#     count = 0
#     text = re.findall("jd's test item", page)
#     for i in text:
#         count+=1
#     assert count == 2
#
# def test_DeleteItem():
#     browser.find_element_by_xpath("/html/body/ul/li[last()]/form").click()
#     page = browser.page_source
#     count = 0
#     text = re.findall("jd's test item", page)
#     for i in text:
#         count+=1
#     assert count == 1
#     browser.close()

##SPRINT 2
browser = webdriver.Chrome()

def test_DisplayUniqueListofItems():
    login("myusername","mypassword")
    addItems("only for myusername")
    browser.get("http://127.0.0.1:8000/accounts/logout")
    login("admin", "adminpassword")
    check = 0
    if "only for myusername" in browser.page_source:
        check = 1
    assert check == 0

def test_TimestampInTodo():
    addItems("Hey!")
    assert "a.m." or "p.m." in browser.page_source
