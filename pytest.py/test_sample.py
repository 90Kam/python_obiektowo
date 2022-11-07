from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
def test_setup():
    
    global driver
    s=Service('D:/PythonProjects/selenium podstawy/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    
    
    driver.implicitly_wait(10)
    driver.maximize_window()
    
def test_page_title():
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page_title = driver.title
    assert page_title == 'onet.pl'

def test_login():
    
    driver.find_element(By.NAME,'username').send_keys('Admin')
    
    
def test_password():
    driver.find_element(By.NAME,'password').send_keys('admin123')
    
def logging_in():
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
   
    time.sleep(5)
    

def test_tear_down():
    
    time.sleep(10)

    driver.close()
    driver.quit()

    print('Test Completed')
    
