idade = int(input('Digite a sua idade: '))

print(f'A sua idade é {idade}')

# SE idade for maior ou igual a 18
if idade >= 18:
    print('Você pode entrar na festa!!!')

elif 16 <= idade < 18:
    print('Você não pode entrar na festa!')

# Se idade não for ...
else:
    print('Meu querido(a) vá pra casa!')