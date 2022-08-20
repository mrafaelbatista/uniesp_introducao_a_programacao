'''
1 - Criar uma variável de ambiente
2 - Instalar o requests e o BeautifulSoup4
'''
import requests
import csv
from bs4 import BeautifulSoup


f = csv.writer(open('m-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []

for i in range(3, 7):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anM' + str(i) + '.htm'
    pages.append(url)


for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')

        f.writerow([names, links])