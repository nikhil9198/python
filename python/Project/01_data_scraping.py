import requests
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
req=requests.get(url)
# print(req)

soup=BeautifulSoup(req.text, "html.parser")
print(soup)