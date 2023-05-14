numero = int(input("Digite um número: "))

if numero > 10:
    print(f'O número é maior do que 10 - {numero}')
elif numero < 10:
    print(f'O número é menor do que 10 - {numero}')
else:
    print(f'Número inválido! {numero}')