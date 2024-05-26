from selenium import webdriver
import time



from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.CSS_SELECTOR, 'a[href="/windows/new"]').click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
h3Title= driver.find_element(By.TAG_NAME, "h3").text
print(f'h3 title is: '+ h3Title)
time.sleep(3)
driver.switch_to.window(windowsOpened[0])
time.sleep(3)
h3Title_mainPage= driver.find_element(By.TAG_NAME, "h3").text
print(f'Main page h3 title is: '+ h3Title_mainPage)
assert "Opening a new window" == h3Title_mainPage
