import requests
from bs4 import BeautifulSoup
import json
import time

# Number of pages to crawl
num_pages = 10

# URL template for Google search results
url_template = 'https://www.google.com/search?q=site:https://en.photo-ac.com/creator-profile/&start={}'

# List to store URLs
urls = []

# Crawl search result pages and extract URLs
for i in range(num_pages):
    url = url_template.format(i * 10)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(i)
    for a in soup.find_all('a'):
        href = a.get('href')
        if href.startswith('/url?q='):
            url = href[7:].split('&')[0]
            if "https://en.photo-ac.com/creator-profile" in url:
                urls.append(url)

    time.sleep(5)

# Save URLs to a JSON file
with open('urls-1.json', 'w') as f:
    json.dump(urls, f)

