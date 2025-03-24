from seleniumbase import Driver
from bs4 import BeautifulSoup
import time
driver = Driver(uc=True)
page = 0
page_increment = 10
# url = f"https://www.indeed.com/jobs?q=software+engineer&l=Thousand+Oaks%2C+CA&radius=50&start={page}&vjk=01eb7b5355d47878"
# url = "https://www.indeed.com/jobs?q=software+engineer&l=Thousand+Oaks%2C+CA&radius=50&start=0&vjk=01eb7b5355d47878"
# driver.uc_open_with_reconnect(url, 4)
# driver.uc_gui_click_captcha()
list_of_urls = []
while page < 30:
    time.sleep(2)
    page += page_increment
    url = f"https://www.indeed.com/jobs?q=software+engineer&l=Thousand+Oaks%2C+CA&radius=50&start={page}&vjk=01eb7b5355d47878"
    driver.uc_open_with_reconnect(url, 4)
    driver.uc_gui_click_captcha()
# Save the page source to an HTML file
    #with open("software.html", "w", encoding="utf-8") as file:
    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")
    job_titles = soup.find_all("h2", class_="jobTitle")
    for job in job_titles:
        title = job.get_text(strip=True)
        link = job.find("a")["href"] if job.find("a") else "No link"
        full_link = f"https://www.indeed.com{link}" if link != "No link" else "No link"
        list_of_urls.append(f"{full_link}")
        print(f"Title: {title}, Link: {full_link}")

# Write the list of URLs to a file
with open("job_links.txt", "w", encoding="utf-8") as file:
    for item in list_of_urls:
        file.write(f"{item}\n")

driver.quit()