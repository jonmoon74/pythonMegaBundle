import requests
from bs4 import BeautifulSoup as bs

url = "https://www.century21.com/for-sale-homes/Rock-River-WY-18560c?src=view"
r = requests.get(url)
c = r.content
print(c)
