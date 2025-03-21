from bs4 import BeautifulSoup

# Read the HTML file
with open("example2.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

company = soup.find('div', attrs={'data-testid': 'inlineHeader-companyName'}).get_text()
location = soup.find('div', attrs={'data-testid': 'inlineHeader-companyLocation'}).get_text()
salaryAndJobType = soup.find('div', id='salaryInfoAndJobType').get_text()
jobDescription = soup.find('div', id='jobDescriptionText').get_text()

print(company)
print(location)
print(salaryAndJobType)
print(jobDescription)