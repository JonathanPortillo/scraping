from bs4 import BeautifulSoup
 
 # Read the HTML file
with open("9.html", "r", encoding="utf-8") as file:
  html_content = file.read()
 
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

company = soup.find(attrs={'class': lambda x: x and 'companyName' in x}).get_text()
location = soup.find(attrs={'data-testid': lambda x: x and 'location' in x or x and 'Location' in x}).get_text()
salary = soup.find('li', attrs={'data-testid': 'list-item'}).get_text()
jobDescription = soup.find('div', id='jobDescriptionText').get_text()

print(company)
print(location)
print(salary)
print(jobDescription)