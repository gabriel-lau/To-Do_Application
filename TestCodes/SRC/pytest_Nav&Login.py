from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

def NavigateToDoPage():
    browser.get("http://127.0.0.1:8000/todo/")
    #returns the heading To-Do List
    return browser.find_element_by_xpath("//h1")

def NavigateToDoHistory():
    browser.get("http://127.0.0.1:8000/todohist/")
    #returns the heading To-Do History
    return browser.find_element_by_xpath("//h1")

def LoginCorrectly():


def LoginIncorrectly():
    




browser = webdriver.Chrome()
NavigateToDoPage()
NavigateToDoHistory()

