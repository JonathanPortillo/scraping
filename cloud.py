# pip3 install cloudscraper beautifulsoup4
from bs4 import BeautifulSoup
import cloudscraper
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# create a cloudscraper instance
scraper = cloudscraper.create_scraper(
    browser={
        "browser": "chrome",
        "platform": "windows",
    },
)

# specify the target URL
url = "https://www.indeed.com/l-Los-Angeles"

# request the target website
response = scraper.get(url)
print(response.status_code)
# get the response status code
print(f"The status code is {response.status_code}")

# parse the returned HTML
soup = BeautifulSoup(response.text, "html.parser")

# get the description element
page_description = soup.select_one(".font-semibold.text-display-md.leading-display-md")

# print the description text
print(page_description.text)

# Set up the WebDriver (ensure you have the correct path to your driver)
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the Indeed job search page
driver.get("https://www.indeed.com/jobs?q=software+engineer&l=Los+Angeles&vjk=e34b655aa7c6f514")

# Wait for a few seconds to let the page load
time.sleep(5)

# Save the entire page source to an HTML file
with open("indeed_jobs.html", "w", encoding="utf-8") as file:
    file.write(driver.page_source)

# Print the title of the page (to verify it's working)
print(driver.title)

# Close the browser
driver.quit()
