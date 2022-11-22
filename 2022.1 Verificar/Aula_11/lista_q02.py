from random import sample


lista = []

for i in range(3):

    lista_auxiliar = sample(range(0, 10), 3)
    lista.append(lista_auxiliar)

print(f'A lista é {lista}')

# Somando todos os valores da matriz
resultado_soma = 0

for linha in lista:

    for coluna in linha:
        resultado_soma = resultado_soma + coluna

print(f'O valor da soma dos itens da matriz é: {resultado_soma}')

# Somando os valores da digonal principal
soma_diagnoal_principal = 0
for l in range(len(lista)):

    for c in range(len(lista[l])):

        if l == c:
            soma_diagnoal_principal += lista[l][c]

print(f'O valor da soma da diagonal principal é: {soma_diagnoal_principal}')

# Diagonal secundária

resultado_diagonal_secundaria = 0

for l in range(len(lista)):
    resultado_diagonal_secundaria += lista[l][(len(lista)-1-l)]

print(f'O valor da soma da diagonal secundaria é: {resultado_diagonal_secundaria}')