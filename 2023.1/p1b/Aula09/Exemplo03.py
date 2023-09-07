import random

n_colunas = int(input('Digite o número de colunas: '))
n_elementos = int(input('Digite o número de elementos: '))

matriz = []

for i in range(n_colunas):
    lista = []

    for j in range(n_elementos):
        lista.append(random.randint(10, 99))

    matriz.append(lista)

for lista in matriz:
    print(lista)

if len(matriz) == len(matriz[0]):

    lista_central = len(matriz) // 2
    print(f'O valor da lista central é {lista_central}')
    meio_da_matriz2 = lista_central
    print(f'O valor da lista central é {meio_da_matriz2}')
    print(matriz[lista_central-1][lista_central-1])
    print(matriz[meio_da_matriz2][lista_central]-1)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            print(matriz[i][j])