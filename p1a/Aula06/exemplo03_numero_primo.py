n = 1001

while n != 1000:

    # Solicita um valor do usuário
    n = int(input('Digite um número:'))

    # Identifica se é número primo ou não
    p = 's'

    for v in range((n-1), 1, -1):
        if (n % v) == 0:
            p = 'n'

    if p == 's':
        print('Este número é primo')
    else:
        print('Este número não é primo')
