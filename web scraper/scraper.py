import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.geeksforgeeks.org/")

content = BeautifulSoup(req.content, "html.parser")

print(content.prettify())