import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import re


url = "https://shop.mango.com/qa-en/women/featured/sale-50-off_d17456481"
r = requests.get(url)

# Extraire le code HTML de r 
soup = BeautifulSoup(r.text, "html.parser")
#print(r.text)
#print(soup)

elements = soup.find_all('ul')



for i in elements:
    print(i)