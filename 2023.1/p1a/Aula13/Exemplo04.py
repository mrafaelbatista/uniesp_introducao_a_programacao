import csv

lista_frutas = [
    ['Pêra', 'Banana'],
    ['Uva', 'Pitaya'],
    ['Maçã', 'Canela'],
    ['Côco', 'Açaí']]

with open('arquivo.csv', 'w',
          newline='', encoding='utf-8') as file:
    escritor = csv.writer(file, delimiter=';')
    escritor.writerows(lista_frutas)