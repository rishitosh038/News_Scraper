import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
response = requests.get(URL)

if response.status_code != 200:
    print("Failed to retrieve the page")
    exit()

soup = BeautifulSoup(response.content, "html.parser")
headlines = []

for h2 in soup.find_all("h2"):
    headline_text = h2.get_text(strip=True)
    if headline_text and headline_text not in headlines:
        headlines.append(headline_text)

with open("headlines.txt", "w", encoding="utf8") as file:
    for idx, headline in enumerate(headlines, start = 1):
        file.write(f"{idx}.{headline}\n")

print(f"{len(headlines)} headlines saved to headlines.txt")