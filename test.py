import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

# Target URL (Replace with an allowed website)
URL = "https://www.indeed.com/jobs?q=software+engineer&l=Los+Angeles"

# Headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
}

r = requests.get(URL, headers=HEADERS)
print(r.status_code)

# # Initialize SQLite database
# def init_db():
#     conn = sqlite3.connect("properties.db")
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS properties (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT,
#             price TEXT
#         )
#     """)
#     conn.commit()
#     conn.close()

# # Store data in SQLite database
# def store_in_db(title, price):
#     conn = sqlite3.connect("properties.db")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO properties (title, price) VALUES (?, ?)", (title, price))
#     conn.commit()
#     conn.close()

# def scrape_properties():
#     session = requests.Session()
#     response = session.get(URL, headers=HEADERS)
    
#     # Print the status code for debugging
#     print(f"Status Code: {response.status_code}")
    
#     if response.status_code == 200:
#         # Save the entire response data to an HTML file
#         with open("response.html", "w", encoding="utf-8") as file:
#             file.write(response.text)
        
#         soup = BeautifulSoup(response.text, "html.parser")
        
#         # Find the container div with class 'HomeCardsContainer'
#         container = soup.find("div", class_="mosaic mosaic-provider-jobcards mosaic-provider-hydrated")
        
#         if container:
#             # Find all divs within the container
#             properties = container.find_all("div")
            
#             # Save all the divs to an HTML file
#             with open("properties.html", "w", encoding="utf-8") as file:
#                 for prop in properties:
#                     file.write(str(prop))
#                     file.write("\n")

#             # Find all property cards
#             property_cards = soup.find_all('a', class_='bp-Homecard__Photo')

#             # Open a CSV file to write the data
#             with open('property_data.csv', mode='w', newline='') as file:
#                 writer = csv.writer(file)
#                 writer.writerow(['href', 'title'])  # Write the header row

#                 # Extract href and title for each property card and write to the CSV file
#                 for card in property_cards:
#                     href = card.get('href')
#                     title = card.get('title')
#                     writer.writerow([href, title])

#             print("Data has been written to property_data.csv")
#         else:
#             print("No properties found in the container.")
#     else:
#         print("Failed to retrieve the webpage.")
#         print(f"Response Content: {response.text}")

# if __name__ == "__main__":
#     init_db()
#     scrape_properties()
