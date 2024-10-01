import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.ca/s?k={query}")
time.sleep(2)
element = driver.find_element(By.CLASS_NAME, "puis-card-container")
print(element.get_attribute("outerHTML"))


driver.close()