import pytest
from SRC.pytest_NavandLogin import *

#Testing Navigation and Login
def test_Login():
    assert "To-Do List"

def test_InvalidLogin():
    assert "You have entered the wrong username/password. Please try again!"

def test_NavigateToDoPage():
    assert "To-Do List"

def test_NavigateToDoHistory():
    assert "To-Do History"
