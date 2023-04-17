while True:
    num = int(input('Digite um número:'))

    if (num % 2) == 0 or num == 0:
        print(f'O número {num} é PAR')
    else:
        print(f'O número {num} é ÍMPAR')