valor1 = float(input('Digite um número: '))
valor2 = float(input('Digite outro número: '))

if valor1 > valor2:
    print(f'O valor1 {valor1} é maior que {valor2}')
elif valor2 > valor1:
    print(f'O valor2 {valor2} é maior que {valor1}')
else:
    print('O valor são inválidos!')