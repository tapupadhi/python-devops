import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000/base')
time.sleep(5)

task = driver.find_element(by=By.XPATH, value='/html/body/form/input')
task.send_keys('new task')

add = driver.find_element(by=By.XPATH, value='/html/body/form/button')
add.click()
time.sleep(5)

delete = driver.find_element(by=By.XPATH, value='/html/body/a')
delete.click()
time.sleep(5)

driver.close()
driver.quit()
