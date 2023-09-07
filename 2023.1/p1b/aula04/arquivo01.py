idade = int(input("Digite sua idade: "))

if idade > 17:
    print("Essa pessoa pode entrar na festa!")
elif idade > 16 and idade < 18:
    print("Mostre sua carteirinha")
else:
    print("Você não pode entrar na festa!")