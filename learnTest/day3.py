import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.baidu.com")

#driver.find_element_by_css_selector('#kw').send_keys('杨幂')
driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('杨幂')
driver.find_element_by_css_selector('#su').submit()
print(driver.title)
