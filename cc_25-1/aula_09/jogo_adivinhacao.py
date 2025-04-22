from random import randint

numero = randint(1, 100)
tentativas = int(input('Escolha quantas tentativas: '))

for i in range(tentativas):
    palpite = int(input('Qual o seu palpite: '))

    if numero == palpite:
        print('Você acertou!')
        break
    elif palpite < numero:
        print('O seu palpite foi abaixo do número!')
    elif palpite > numero:
        print('O seu palpite foi ACIMA do número!')

