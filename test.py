import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import re


url = "https://shop.mango.com/qa-en/women/coats_c67886633"
r = requests.get(url)

# Extraire le code HTML de r 
soup = BeautifulSoup(r.text, "html.parser")
#print(soup)

div = soup.find_all("div", {"class": "page tRkeN"})
print(div)


elements = soup.find_all('ul', {"class": "LSqil"})
print(elements)
'''
for ul_element in elements:
    #extraire lien produit 
    liens_href = [a['href'] for a in ul_element.find_all('a')]
    
    # Afficher les liens extraits
    for lien in liens_href:
        print(lien)

# Itérer sur les pages
for page in pages:
    # Extraire le contenu de la page
    extracted_page = page.text

    # Ajouter la page extraite à la liste
    extracted_pages.append(extracted_page)

# Afficher les pages extraites
for page in extracted_pages:
    print(page)'''


'''liens_valides=[]
for ul_element in elements:
    #extraire lien produit 
    liens_href = [a['href'] for a in ul_element.find_all('a')]
    
    
    # Vérifier la validité de chaque lien
    for lien in liens_href:
        if lien.startswith("http") or lien.startswith("https"):
            try:
                response = requests.head(lien)
                if response.status_code == 200:
                    liens_valides.append(lien)
                    print(f"Lien valide : {lien}")
                else:
                    print(f"Lien non valide ({response.status_code}) : {lien}")
            except requests.RequestException as e:
                print(f"Erreur lors de la vérification du lien : {lien}, erreur : {e}")
'''