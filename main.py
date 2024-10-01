import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.udemy.com/")
assert "Udemy" in driver.title
time.sleep(2)
print(driver.title)

# Find the search bar using its name attribute

search_bar = driver.find_element(By.NAME, "q")
search_bar.clear()

search_bar.send_keys("Python")
time.sleep(2)
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

# search_bar.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# Print the current URL
print(driver.current_url)

time.sleep(5)
driver.close()