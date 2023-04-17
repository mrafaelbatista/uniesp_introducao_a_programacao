# matriz = [(1, 2, 3, 9, 8), [2, 4, 6], [4, 8, 12], [15, 30, 45]]

# print(len(matriz))
# print(len(matriz[0]))

# for i in range(len(matriz)):

#     for j in range(len(matriz[i])):

#         print(matriz[i][j])

# for linha in matriz:

#     for coluna in linha:

#         print(coluna)

# lista_nomes = ['Miguel', 'Gabriel', 'Rafael']

# for nome in lista_nomes:
#     print(nome)

# for numero in range(2, 10, 4):
#     print(numero)

mtz = [
    [78, 90, 100, 98, 7],
    [56, 72, 93, 77, 93],
    [10, 4, 73, 77, 93],
    [78, 90, 100, 77, 93],
    [10, 4, 73, 90, 100]
]

# l = linha / c = coluna
for l in range(len(mtz)):
    
    for c in range(len(mtz[l])):

        if l == c:
            print(mtz[l][c])
            
        if (mtz[l][c] % 2) == 0:
            print(f"{mtz[l][c]} -> É par!")
        else:
            print(f"{mtz[l][c]} -> É ímpar!!")
