import csv

lista = ['abacate', 'uva', 'kiwi']

with open('exemplo02.csv','w',newline='',
        encoding='utf-8') as arquivo:

    writer = csv.writer(arquivo, delimiter=';')
    writer.writerow(lista)