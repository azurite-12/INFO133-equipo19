#Script que genera el documento csv de información del IDH

from bs4 import BeautifulSoup
import requests
#import string
import pandas as pd
import csv

#pip install html5lib, beautifulsoup4 y lxml

wiki_url = 'https://es.wikipedia.org/wiki/Anexo:Comunas_de_Chile'

respuesta = requests.get(wiki_url)
soup = BeautifulSoup(respuesta.text, 'html.parser')

tabla_idh = soup.find('table').find_all('tr')
#dfr = pd.read_html(str(tabla_idh))
#print(dfr)

comunas_lista = []
for row in tabla_idh:
    cells = row.find_all('td')
    row_data = [cell.get_text(strip=True) for cell in cells]
    comunas_lista.append(row_data)

with open('tablaidh.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(comunas_lista)

print("")
print(comunas_lista)