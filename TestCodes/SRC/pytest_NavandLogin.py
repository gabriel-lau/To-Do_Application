# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import pytest
#
# def login(username, password):
#     browser.get("http://127.0.0.1:8000/todo")
#     user = browser.find_element_by_name("username").send_keys(username)
#     passwrd = browser.find_element_by_name("password").send_keys(password)
#     browser.find_element_by_xpath("//input[@value='login']").click()
#
# def NavigateToDoPage():
#     browser.get("http://127.0.0.1:8000/todo/")
#     #returns the heading To-Do List
#     return browser.find_element_by_xpath("//h1")
#
# def NavigateToDoHistory():
#     browser.get("http://127.0.0.1:8000/todohist/")
#     #returns the heading To-Do History
#     return browser.find_element_by_xpath("//h1")
#
#
#
#
#
#
# browser = webdriver.Chrome()
# login("myusername", "mypassword")
# NavigateToDoPage()
# NavigateToDoHistory()
# # browser.close()
