import csv

with open('exemplo01.csv', 'r', newline='', encoding='utf-8') as arquivo:
    arquivo_lido = csv.reader(arquivo, delimiter=';')
    # print(arquivo_lido)

    for linha in arquivo_lido:
        #print(linha)

        if int(linha[1]) >= 30:
            print(f'A pessoa {linha[0]} tem mais de 30 anos!')
