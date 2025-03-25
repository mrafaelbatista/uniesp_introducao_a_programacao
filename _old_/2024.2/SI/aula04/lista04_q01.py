nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if 0 <= media <= 10:
    if  media >= 6:
        print('Parabéns, você foi aprovado!')
        print(f'Sua nota foi {media}')
    else:
        print('Perdeu! Ano que vem nos vemos de novo!!!')
        print(f'Sua nota foi {media}')
else:
    print('Valor incorreto!')



