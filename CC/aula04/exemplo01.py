idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você pode entrar na nossa festa!')

elif idade >= 12 and idade <= 17:
    print('Pode entrar, na área Teen!')

else:
    print('Infelizmente, você não tem idade!')
