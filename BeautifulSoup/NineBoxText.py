import requests
from bs4 import BeautifulSoup

url = "https://change-effect.com/2014/09/15/the-9-box-model-explained/"
url2 = "https://www.instapaper.com/read/1216818587"
res = requests.get(url2)
c = res.content

soup = BeautifulSoup(c, 'html.parser')
print(soup)
