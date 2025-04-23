salario = float(input('Digite seu salário: '))

if 0 < salario <= 2000:
    print('Salário isento de imposto de renda!')

elif 2000 < salario <= 3500:
    imposto = salario * 0.10
    print(f'O imposto é R$ {imposto}')

elif salario > 3500:
    imposto = salario * 0.15
    print(f'O imposto é R$ {imposto}')

else:
    print('Valor inválido!')
