import requests
import time
from fake_useragent import UserAgent

# Generate a random user-agent
ua = UserAgent()
headers = {
    'User-Agent': ua.random
}

url = 'https://www.indeed.com/jobs'
params = {'q': 'software developer', 'l': 'New York'}

# Use a session to keep cookies and headers consistent across requests
with requests.Session() as session:
    session.headers.update(headers)

    try:
        response = session.get(url, params=params)
        if response.status_code == 200:
            # Process the page
            print(response.text)
        else:
            print(f"Encountered error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    time.sleep(10)  # Wait 10 seconds before the next request