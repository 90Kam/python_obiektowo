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

def test_login():
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.find_element(By.NAME,'username').send_keys('Admin')
    driver.find_element(By.NAME,'password').send_keys('admin123')
    driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
    driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()

def test_tear_down():
    
    time.sleep(3)

    driver.close()
    driver.quit()

    print('Test Completed')