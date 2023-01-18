import requests
from bs4 import BeautifulSoup


scrape = requests.get("https://quotes.toscrape.com/",
timeout = 5)

req = BeautifulSoup(scrape.text, "html.parser")

names = req.findAll("small", attrs={"class":"author"})
quotes = req.findAll("span", attrs={"class":"text"})




for quote in quotes:
    print(quote.text)

for name in names:
    print(name.text)
