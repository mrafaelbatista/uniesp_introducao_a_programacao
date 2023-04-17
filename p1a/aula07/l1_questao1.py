num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num2 > num1:
    print(f'{num2} é maior que {num1}')
else:
    print(f'{num1} e {num2} são iguais!')