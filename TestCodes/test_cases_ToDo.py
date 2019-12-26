import pytest
from SRC.pytest_ToDo import *
import re

# Functions
def addItems(string):
    input = browser.find_element_by_name("content")
    input.send_keys(string)
    input.send_keys(Keys.RETURN)
    return True

#Test Cases
def test_DisplayListOfItems():
    assert "List of Items"

def test_AddBlankItem():
    browser.find_element_by_xpath("//input[@value='Add']").click()
    assert "error" in browser.page_source

def test_AddValidItem():
    addItems("jd's test item")
    assert "jd's test item" in browser.page_source

def test_AddExistingItem():
    addItems("jd's test item")
    page = browser.page_source
    count = 0
    text = re.findall("jd's test item", page)
    for i in text:
        count+=1
    assert count == 2
