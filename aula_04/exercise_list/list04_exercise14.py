# Solicita ao usuário que insira seu salário mensal
salario = float(input("Digite o valor do seu salário mensal: "))

# Calcula o imposto de renda com base nas faixas de salário
if salario <= 2000:
    imposto = 0  # Isento de imposto
elif salario <= 3500:
    imposto = salario * 0.10  # 10% de imposto para salários entre R$2000,01 e R$3500
else:
    imposto = salario * 0.15  # 15% de imposto para salários acima de R$3500

# Imprime o valor do imposto de renda calculado
print("O valor do imposto de renda é R$", imposto)
