from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/upload-download-test/index.html')
driver.find_element(By.ID,"downloadButton").click()