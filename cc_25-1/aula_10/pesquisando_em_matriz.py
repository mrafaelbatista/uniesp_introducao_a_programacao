from random import randint

matriz = []

for j in range(3):
    lista_temporaria = []

    for i in range(3):
        lista_temporaria.append(randint(0, 1000))

    matriz.append(lista_temporaria)

maior = -1

# Percorrer a matriz utilizando o conceito de vetores e matrizes
for linha in range(len(matriz)):

    for coluna in range(len(matriz[linha])):
        if maior < matriz[linha][coluna]:
            maior = matriz[linha][coluna]

print(f'O maior valor é: {maior}')
print(matriz)