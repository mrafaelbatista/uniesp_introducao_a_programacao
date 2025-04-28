import time
from random import randint

MIN = 0
MAX = 1000
QTD_ITEM = 10
vetor10 = []

# Preparação do Vetor
for i in range(QTD_ITEM):
    vetor10.append(randint(MIN, MAX))

# Buscar o maior valor do vetor
maior_valor = MIN
posicao = MIN

for i in range(len(vetor10)):
    print(f'Iniciando o ciclo {i}')
    print(f'Maior Valor: {maior_valor} e Vetor: {vetor10[i]}')
    if maior_valor < vetor10[i]:
        maior_valor = vetor10[i]
        posicao = i

    time.sleep(2)

print('O Vetor 10 completo:')
print(vetor10)
print(f'Maior valor: {maior_valor}')
print(f'Posição / Índice: {posicao}')
