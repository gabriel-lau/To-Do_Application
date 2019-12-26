import pytest
from SRC.pytest_ToDo import *
import re

#Test Cases
def test_DisplayListOfItems():
    assert "List of Items"

def test_AddBlankItem():
    browser.find_element_by_xpath("//input[@value='Add']").click()
    assert "error" in browser.page_source
