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

@pytest.mark.parametrize("a,b",[
("myusername", "wrongpassword"),
("wrongusername", "wrongpassword"),
]
)
def test_InvalidLogin(a,b):
    browser.get("http://127.0.0.1:8000/accounts/login/")
    login(a,b)
    assert "Incorrect username and password. Please try again."

# def test_CannotNavigateToDoPage():
#     assert ""
#
# def test_CannotNavigateToDoHistory():
#     assert ""
