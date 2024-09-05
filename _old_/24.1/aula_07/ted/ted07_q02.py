from random import randint

# Inicializa a matriz A como uma lista de listas vazias
A = []

# Preenche a matriz A com valores inteiros aleatórios entre 0 e 9
for _ in range(10):
    linha = []
    for _ in range(10):
        linha.append(randint(0, 9))
    A.append(linha)

# Imprime a matriz A no terminal
print("Matriz A:")
for linha in A:
    print(linha)

# Calcula a soma de todos os valores da matriz A
soma_A = 0
for linha in A:
    for valor in linha:
        soma_A += valor

# Imprime a soma de todos os valores da matriz A
print("\nSoma de todos os valores da matriz A:", soma_A)

# Inicializa a matriz B como uma lista de listas vazias
B = []

# Preenche a matriz B com os valores da matriz A multiplicados por 3
for linha in A:
    linha_B = [valor * 3 for valor in linha]
    B.append(linha_B)

# Imprime a matriz B no terminal
print("\nMatriz B (valores da matriz A multiplicados por 3):")
for linha in B:
    print(linha)
