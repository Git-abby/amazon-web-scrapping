
import time

from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
query = "laptop"
file = 0
for i in range(1, 20):
    try:
        driver.get(f"https://www.amazon.ca/s?k={query}&page={i}")
        elements = driver.find_elements(By.CLASS_NAME, "puis-card-container")

        time.sleep(2)
        print(f"Page {i}: {len(elements)} elements found")

        for elem in elements:
            d = elem.get_attribute("outerHTML")
            with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
                f.write(d)
                file += 1

    except Exception as e:
        print(f"Exception on page {i}: {e}")

driver.quit()
