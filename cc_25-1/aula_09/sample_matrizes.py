matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimindo a matriz
print(matriz)
# Imprimir a segunda linha da matriz
print(matriz[1])
print(matriz[1][2])

# O desafio é percorrer a matriz mostrando
# todos os números em separado
print('--- Solução do Desafio ---')
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])