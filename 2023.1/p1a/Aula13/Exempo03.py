import csv

arquivo = 'meu_arquivo.csv'
with open(arquivo, 'r', newline='', encoding='UTF-8') as file:

    arquivo_lido = csv.reader(file, delimiter=';')

    for linha in arquivo_lido:
        print(f'Tamanho da lista: {len(linha)} | Conteúdo: {linha}')
        print(f'Nome do amigo ou amiga é: {linha[0]}')