lista_de_listas = [
    [0, 1, 2, 3, 4, 5],
    [0, 1, 2, [0, 1, 2, 3, 4, 5], 4, 5],
    [0, 1, 2, 3, 4, 5]
]

dicionario_de_listas = {
    'frutas': ['pera', 'uva', 'morango'],
    'carros': ['Fusca', 'Monza', 'Opala'],
    'numeros': [0, 1, 2, 3, 4, 5]
}

print(dicionario_de_listas['frutas'][2])

print(lista_de_listas[1][3][0])

# for lista in lista_de_listas:
#     for l in lista:
#         print(l)