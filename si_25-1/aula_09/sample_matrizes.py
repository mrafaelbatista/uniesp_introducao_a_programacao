import time

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimindo a matriz
print(matriz)

# Imprimir a segunda linha da matriz
print(matriz[1])

# Imprimir o número 6 apenas
print(matriz[1][2])

# Exercício de exemplo:
# Imprima cada um dos números desta matriz
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'i={i} e j={j} - {matriz[i][j]}')
        time.sleep(1)