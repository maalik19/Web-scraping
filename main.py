import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json



url = "https://shop.mango.com/qa-en/women"
r = requests.get(url)

# Extraire le code HTML de r 
soup = BeautifulSoup(r.text, "html.parser")
#print(soup)

#date
date_web_scraping = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(date_web_scraping )
results = []

# trouver liens 
elements = soup.find_all("div", class_="no-js", id="vsvhome")
#print(elements)

links = []
for element in elements:
    for link in (a['href'] for a in element.find_all('a', href=True)):  
        if (link == "//shop.mango.com/redirect.faces?op=conta&externa=CATSHE112021MANGOGIRLS") or (link =="//shop.mango.com/redirect.faces?op=conta&seccion=rebajas_she&tiendaid=she"):
            links.append("https:"+link)
        else: links.append("https://shop.mango.com" + link)

valid_links = []
for link in links:
    if (link != "https://shop.mango.com#nolink") and (link != "https://shop.mango.com/qa-en/teen") and (link != "https://shop.mango.com/qa-en/kids") and (link != "https://shop.mango.com/qa-en/men") :  # Skip the specific link
        try:
            response = requests.head(link, allow_redirects=True)
            response.raise_for_status()  #  exception non-200 
            valid_links.append(link)
        except requests.exceptions.RequestException as e:
            print(f"Invalid link: {link} ({e})")




#affichage lien
print("Valid links:")
for link in valid_links:
    print(link)

'''
for link in links:
    article_response = requests.get(article_url)
    article_soup = BeautifulSoup(article_response.content, 'html.parser')
    
    # Extract information from the article page
    brand = "Mango"
    gender = "women"
    category = article_soup.find('meta', {'property': 'og:title'})['content']
    product_name = article_soup.find('h1', {'class': 'product-name'}).text.strip()
    colors = [color.text.strip() for color in article_soup.find_all('div', {'class': 'color'})]
    description = article_soup.find('meta', {'property': 'og:description'})['content']
    description_link = article_url
    possible_sizes = [size.text.strip() for size in article_soup.find_all('div', {'class': 'size'})]
    images = [img['src'] for img in article_soup.find_all('img', {'class': 'she'})]

    # Store the extracted information in a dictionary
    article_info = {
        "date_web_scraping": date_web_scraping,
        "brand": brand,
        "gender": gender,
        "category": category,
        "product_name": product_name,
        "colors": colors,
        "description": description,
        "description_link": description_link,
        "possible_sizes": possible_sizes,
        "images": images
    }

    results.append(article_info)


    results.append(article_info)

for data in results:
    print(data)

# Convertir the list of resultat to a JSON string
json_data = json.dumps(results, indent=4)

# ecrire
with open("products.json", "w") as outfile:
    outfile.write(json_data)

print("JSON file created successfully!")'''