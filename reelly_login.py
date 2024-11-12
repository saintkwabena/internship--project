from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://soft.reelly.io/sign-in')


driver.find_element(By.ID , 'email-2' ).send_keys('elkwabena@gmail.com')
driver.find_element(By.ID , 'field').send_keys('FMlithonia1!')

driver.find_element(By.XPATH , "//a[@class='login-button w-button']").click()

driver.find_element(By.CSS_SELECTOR , "a.menu-button-block.w-inline-block.w--current").click()

sleep(6)