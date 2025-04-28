from random import randint
import time

matriz = []

for i in range(10):
    lista_temporaria = []

    for j in range(10):
        lista_temporaria.append(randint(1, 1000))
    matriz.append(lista_temporaria)

maior_valor = -1
posicao = -1

for i in range(len(matriz)):

    for j in range(len(matriz[i])):

        if maior_valor < matriz[i][j]:
            maior_valor = matriz[i][j]
            posicao = [i, j]



