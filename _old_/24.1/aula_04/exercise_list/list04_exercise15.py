# Solicita ao usuário que insira a velocidade atual do carro
velocidade = float(input("Digite a velocidade atual do carro em km/h: "))

limite_velocidade = 80  # Limite de velocidade em km/h

# Verifica se o carro está abaixo do limite de velocidade ou se deverá ser multado
if velocidade <= limite_velocidade:
    print("O carro está dentro do limite de velocidade.")
else:
    # Calcula a quantidade de km/h acima do limite
    km_acima = velocidade - limite_velocidade
    # Calcula o valor da multa (R$5,00 por km acima do limite)
    multa = km_acima * 5
    print(f"O carro está acima do limite de velocidade. A multa será de R${multa:.2f}.")
