from random import randint

# Inicializa um vetor vazio para armazenar os números
vet = []

# Gera 10 números aleatórios entre 0 e 5 e armazena no vetor
for _ in range(10):
    num = randint(0, 5)
    vet.append(num)

print(vet)

# Inicializa um vetor para armazenar as posições dos números repetidos
posicoes_repetidas = []

# Verifica se existem números repetidos e armazena suas posições
for i in range(len(vet)):
    for j in range(i):
        if vet[i] == vet[j]:
            posicoes_repetidas.append(i)
            break  # Se encontrar um número repetido, para a busca

# Exibe os números repetidos e suas posições
if posicoes_repetidas:
    print("Números repetidos e suas posições:")
    for posicao in posicoes_repetidas:
        print(f"O número {vet[posicao]} está repetido na posição {posicao}.")
else:
    print("Não há números repetidos.")
