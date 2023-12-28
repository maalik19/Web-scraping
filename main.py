import requests
from bs4 import BeautifulSoup

"""selectolax
playwright
scrapy
httpx"""


url = "https://shop.mango.com/qa-en/women"
r = requests.get(url)

# Extraire le code HTML de r 
soup = BeautifulSoup(r.text, 'lxml')
#print(r.text)

links =[]
tds = soup.find_all("td")

# lien a href
for td in tds:
    a = td.findall("a")
    link=a['href']
    links.append('https://shop.mango.com/qa-en/women/'+link)
    price = product_item.find("span", class_="product-price").text

print(links)  