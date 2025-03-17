from bs4 import BeautifulSoup

# Read the HTML file
with open("software.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Example: Print the title of the page
print(soup.title.string)

# Example: Find all job titles and print them
job_titles = soup.find_all("h2", class_="jobTitle")
for job in job_titles:
    print(job.get_text(strip=True))