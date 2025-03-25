idade = int(input('Digite sua idade: '))

# idade > 17
if idade >= 18:
    print('Pode ficar na festa de boas!')

# idade > 14 and idade < 18
elif 14 < idade < 18: # inclusivo e não inclusivo
    print('Desapareça daqui!')

else:
    print('Vá tirar a catinga do mijo!')