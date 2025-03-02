import requests
from bs4 import BeautifulSoup
import sqlite3

# Target URL (Replace with an allowed website)
URL = "https://example.com/properties"

# Headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect("properties.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT
        )
    """)
    conn.commit()
    conn.close()

# Store data in SQLite database
def store_in_db(title, price):
    conn = sqlite3.connect("properties.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO properties (title, price) VALUES (?, ?)", (title, price))
    conn.commit()
    conn.close()

def scrape_properties():
    response = requests.get(URL, headers=HEADERS)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Example: Finding property listings by class name
        properties = soup.find_all("div", class_="property-listing")
        
        for prop in properties:
            title = prop.find("h2").text.strip()
            price = prop.find("span", class_="price").text.strip()
            print(f"Title: {title}, Price: {price}")
            store_in_db(title, price)
    else:
        print("Failed to retrieve the webpage.")

if __name__ == "__main__":
    init_db()
    scrape_properties()
