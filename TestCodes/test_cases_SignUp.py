from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

browser = webdriver.Chrome()

def signup(username, password1, password2):
    browser.get("http://127.0.0.1:8000/accounts/signup")
    browser.find_element_by_name("username").send_keys(username)
    browser.find_element_by_name("password1").send_keys(password1)
    browser.find_element_by_name("password2").send_keys(password2)
    browser.find_element_by_xpath("//input[@value='Sign Up']").click()

def test_SignUpWithValidCredentials():
    signup("janinedesiree", "ephemeral12", "ephemeral12")
    assert "Please login to see this page." in browser.page_source

def test_CantSignUpWithExistingUsername():
    signup("janinedesiree", "ephemeral12", "ephemeral12")
    assert "A user with that username already exists." in browser.page_source

def test_InvalidSignupPasswordTooSimilarToInfo():
    signup("testuser1", "testuser1", "testuser1")
    assert "The password is too similar to the username." in browser.page_source
