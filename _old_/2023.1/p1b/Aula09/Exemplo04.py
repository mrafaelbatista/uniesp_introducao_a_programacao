def encontrar_elemento_central(matriz):
    n = len(matriz)
    meio = n // 2 # Posição central da matriz
    if n % 2 == 0:
        elemento_central = matriz[meio-1][meio-1]
    else:
        elemento_central = matriz[meio][meio]
    return elemento_central


matriz = [[0 for j in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        matriz[i][j] = i * 10 + j

for i in matriz:
    print(i)

elemento_central = encontrar_elemento_central(matriz)
print(elemento_central)
