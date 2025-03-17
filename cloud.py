# pip3 install cloudscraper beautifulsoup4
from bs4 import BeautifulSoup
import cloudscraper

# create a cloudscraper instance
scraper = cloudscraper.create_scraper(
    browser={
        "browser": "chrome",
        "platform": "windows",
    },
)

# specify the target URL
url = "https://www.indeed.com/l-Los-Angeles,-CA-jobs.html"

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
