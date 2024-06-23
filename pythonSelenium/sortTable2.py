from selenium import webdriver
import time



from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
tableTitles = driver.find_elements(By.CSS_SELECTOR, 'th[role="columnheader"]')
tableTitles[0].click()
time.sleep(3)
rows = driver.find_elements(By.CSS_SELECTOR, 'table.table tbody tr')

        # Loop through each row and extract the first cell (fruit/vegetable name)
fruit_veg_names = []

for row in rows:
    name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text
    fruit_veg_names.append(name)

names_after_sort = sorted(fruit_veg_names)

print(fruit_veg_names)
print(names_after_sort)

assert fruit_veg_names == names_after_sort, "lists are not identical"

assert tableTitles[0].get_attribute('aria-sort') == 'ascending'

time.sleep(3)
