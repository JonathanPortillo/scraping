from bs4 import BeautifulSoup

# Read the HTML file
with open("software.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Example: Print the title of the page
print(soup.title.string)

list_of_urls = []
# Example: Find all job titles and their links, then print them
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