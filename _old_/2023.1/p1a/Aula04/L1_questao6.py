# Entrada de Dados - Salário
salario = float(input('Digite seu salário: '))

# Processamento - Calcular aumento
if salario <= 1500:
    # Aumento de 15%
    salario = salario * 1.15
else:
    # Aumento de 10%
    salario = salario * 1.1

# Saída - Salário + aumento
print(f'O novo salário é {salario}')