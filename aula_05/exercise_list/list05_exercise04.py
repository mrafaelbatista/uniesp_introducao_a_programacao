moedas_1_real = int(input("Quantidade de moedas de 1 real: "))
moedas_50_centavos = int(input("Quantidade de moedas de 50 centavos: "))
moedas_25_centavos = int(input("Quantidade de moedas de 25 centavos: "))

total = (moedas_1_real * 1) + (moedas_50_centavos * 0.5) + (moedas_25_centavos * 0.25)

print(f"O valor total das moedas é: R${total:.2f}")
