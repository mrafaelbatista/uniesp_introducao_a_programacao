# Matriz representada como lista de listas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Encontrar o maior elemento na matriz
maior_elemento = float('-inf')
for linha in matriz:
    for elemento in linha:
        if elemento > maior_elemento:
            maior_elemento = elemento
print("Maior elemento na matriz:", maior_elemento)
