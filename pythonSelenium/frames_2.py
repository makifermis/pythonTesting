from selenium import webdriver
import time

#chrome driver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/iframe")
#driver.find_element(By.CSS_SELECTOR, "button.tox-notification__dismiss").click()
time.sleep(3)
driver.switch_to.frame("mce_0_ifr")


driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I'm able to automate frames")

time.sleep(3)

