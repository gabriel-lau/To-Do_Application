import pytest
from SRC.pytest_NavandLogin import *

#Testing Navigation and Login
def test_Login():
    assert "To-Do List"

def test_NavigateToDoPage():
    assert "To-Do List"

def test_NavigateToDoHistory():
    assert "To-Do History"

def test_Logout():
    browser.get("http://127.0.0.1:8000/accounts/logout/")
    assert "Logged out" in browser.page_source

# def test_InvalidLogin():
#     assert ""
#
# def test_CannotNavigateToDoPage():
#     assert ""
#
# def test_CannotNavigateToDoHistory():
#     assert ""
