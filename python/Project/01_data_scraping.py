import requests
from bs4 import BeautifulSoup
import pandas as pd

#Step-1: fetch webpage content
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
req=requests.get(url)

#Step-2: parse with BeautifulSoup
soup=BeautifulSoup(req.text, "html.parser")

#Step-3: extracting data
titles=[item.text.strip() for item in soup.find_all("a", class_="title")]
prices=[item.text.strip()for item in soup.find_all("h4", class_="price float-end card-title pull-right")]
description=[item.text.strip()for item in soup.find_all("p", class_="description card-text")]
noOfReviews=[item.text.strip()for item in soup.find_all("p", class_="review-count float-end")]

#Step-3: Storing data in dataform
df=pd.DataFrame({
    "Title": titles,
    "Description": description,
    "Price": prices,
    "Reviews": noOfReviews
})

df.to_excel("laptops_data.xlsx", index=False)
print("Data has been save successfully.!")