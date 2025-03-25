# Solicita ao usuário que insira a temperatura atual
temperatura = float(input("Digite a temperatura atual em graus Celsius: "))

# Verifica a temperatura e fornece a descrição do clima com base nas condições fornecidas
if temperatura < 15:
    print("Está frio.")
elif temperatura >= 15 and temperatura <= 25:
    print("Está ameno.")
else:
    print("Está quente.")
