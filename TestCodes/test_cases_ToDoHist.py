Hist
import pytest
from SRC.pytest_ToDoHist import *
import re

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

##SPRINT 1
#Testing Navigation and Login
# def test_DisplayListofArchivedItems():
#     assert "List of Archived Items"

# def test_ArchiveItem():
#     browser.get("http://127.0.0.1:8000/todo/")
#     browser.find_element_by_xpath("/html/body/ul/li[last()]/form[last()]/input[last()]").click()
#     browser.get("http://127.0.0.1:8000/todohist/")
#     assert "jd's test item" in browser.page_source
#
# def test_ItemDeletedNotArchived():
#     browser.get("http://127.0.0.1:8000/todohist/")
#     page = browser.page_source
#     count = 0
#     text = re.findall("jd's test item", page)
#     for i in text:
#         count+=1
#     assert count == 1

##SPRINT 2
browser = webdriver.Chrome()

def test_DisplayAddedItemToHistList():
    login("myusername","mypassword")
    addItems("only for myusername")
    browser.get("http://127.0.0.1:8000/todohist")
    assert "only for myusername" in browser.page_source

def test_DisplayDeletedInArchive():
    browser.get("http://127.0.0.1:8000/todo")
    addItems("This should be in archive!")
    browser.find_element_by_xpath("/html/body/ul/li[last()]/form").click()
    browser.get("http://127.0.0.1:8000/todohist")
    assert "This should be in archive!" in browser.page_source

def test_DisplayUniqueArchivedListofItems():
    browser.get("http://127.0.0.1:8000/accounts/logout")
    login("admin", "adminpassword")
    browser.get("http://127.0.0.1:8000/todohist")
    check = 0
    if "only for myusername" in browser.page_source:
        check = 1
    assert check == 0
