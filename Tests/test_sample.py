from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
import pytest
from paages import login_page
from locators import user_name,password,logging_in, error_message, admin_button,search_username, search_user_button,delete_user,cancel_delete_user
def test_setup():
    global driver
    s=Service('D:/PythonProjects/selenium podstawy/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    
    global waitin
    waitin = driver.implicitly_wait(10)
    driver.maximize_window()
def test_page_title():
    driver.get(login_page)
    # page_title = driver.title
    # assert page_title == 'onet.pl'
def test_login():
    driver.find_element(By.NAME,user_name).send_keys('Admin')
def test_password():
    driver.find_element(By.NAME,password).send_keys('admin123')
def test_logging_in():
    driver.find_element(By.CSS_SELECTOR,logging_in).click()
    # if driver.find_element(By.XPATH,error_message).text==True:
    #     print(error_message)
    # else:
    #     print('wszystko okej')
    # assert error_message!='Invalid credentials'
def test_admin_button():
    driver.find_element(By.XPATH,admin_button).click()
def test_search_username():
    driver.find_element(By.XPATH,search_username).send_keys('tester')
    time.sleep(3)
def test_search_user_button():
    driver.find_element(By.XPATH,search_user_button).click()
    time.sleep(3)
def test_delete_user():
    driver.find_element(By.XPATH,delete_user).click()
    time.sleep(3)
def test_cancel_delete_user():
    driver.find_element(By.XPATH,cancel_delete_user).click()
    time.sleep(3)
def test_tear_down():
    
    time.sleep(5)

    driver.close()
    driver.quit()

    print('Test Completed')

test_setup()
test_page_title()
test_login()
test_password()
test_logging_in()
test_admin_button()
test_search_username
test_search_user_button()
test_delete_user()
test_cancel_delete_user()
test_tear_down()

