# Implemente um programa que simule o lançamento de um dado de 6
# faces várias vezes, conforme especificado pelo usuário.
# Utilize um loop para realizar os lançamentos e exibir os resultados.
# Informe qual o maior valor e em qual chance

from random import randint
from time import sleep

valor_dado = -1
n_lancamento = 0

# Definição da quantidade de vezes
n = int(input('Digite quantas lançamentos do dados: '))

for i in range(n):

    vlr_lancamento = randint(1, 6)

    if vlr_lancamento > valor_dado:
        valor_dado = vlr_lancamento
        n_lancamento = i + 1

    print(f'NL = {i+1} e Vlr = {vlr_lancamento}')
    sleep(1)

print('===== O maior lançamento =====')
print(f'Maior => {valor_dado} e o lançamento n{n_lancamento}')