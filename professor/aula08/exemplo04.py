# Matrizes representadas como listas de listas
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[4, 3], [2, 1]]

# Subtração das matrizes
subtracao_matriz = [[matriz1[i][j] - matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
print("Subtração das matrizes:")
for linha in subtracao_matriz:
    print(linha)
