# To send HTTP requests
import requests

# To parse HTML content
from bs4 import BeautifulSoup

page_scraped = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_scraped.text, "html.parser")
qoutes = soup.findAll("span", attrs={"class": "text"})
authors = soup.find_all("small", attrs={"class": "author"})

for quote in qoutes:
    print(quote.text)