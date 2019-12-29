import pytest
from SRC.pytest_ToDoHist import *
import re

#Testing Navigation and Login
def test_DisplayListofArchivedItems():
    assert "List of Archived Items"

def test_ArchiveItem():
    browser.get("http://127.0.0.1:8000/todo/")
    browser.find_element_by_xpath("/html/body/ul/li[last()]/form[last()]/input[last()]").click()
    browser.get("http://127.0.0.1:8000/todohist/")
    assert "jd's test item" in browser.page_source

def test_ItemDeletedNotArchived():
    browser.get("http://127.0.0.1:8000/todohist/")
    page = browser.page_source
    count = 0
    text = re.findall("jd's test item", page)
    for i in text:
        count+=1
    assert count == 1
