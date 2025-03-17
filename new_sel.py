from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

service = Service("chromedriver.exe")
# Set up the WebDriver (ensure you have the correct path to your driver)
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")

# Find the search bar using its name attribute and enter a search query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")
search_box.send_keys(Keys.RETURN)  # Press Enter

# Wait for a few seconds to let the results load
time.sleep(100)

# Print the title of the page (to verify it's working)
print(driver.title)

# Close the browser
driver.quit()
