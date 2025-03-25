# entrada de dados
nota_1 = float(input('Digite a nota 1: '))
nota_2 = float(input('Digite a nota 2: '))

# processamento
media = (nota_1 + nota_2) / 2

# saída de dados
if media >= 6:
    print(f'Aprovado, com média {media}.')
else:
    print(f'Recuperação, com média {media}.')


