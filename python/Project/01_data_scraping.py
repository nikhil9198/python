import requests
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
req=requests.get(url)
# print(req)

soup=BeautifulSoup(req.text, "html.parser")
# print(soup)

productsCards=soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
# print(len(productsCards))
#
# titles=soup.find_all("a", class_="title")
# # print(titles)
#
# for item in titles:
#     print(item.txt)

prices=soup.find_all("h4", class_="price float-end card-title pull-right")
# print(titles)
for item in prices:
    print(item.txt)

descriptions=soup.find_all("p", class_="price float-end card-title pull-right")
# print(titles)
for item in prices:
    print(item.txt)