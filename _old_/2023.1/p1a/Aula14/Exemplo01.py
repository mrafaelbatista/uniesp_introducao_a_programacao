# Definição das funções Somar e Subtrair
def soma(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

# Operação desejada
op = int(input('Digite\n1 - Soma\n2 - Subtração'))
# Solicitação de números
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
# Condicional para escolher a operação
resultado = 0
if op == 1:
    resultado = soma(n1, n2)
elif op == 2:
    resultado = subtrair(n1, n2)
else:
    print('Opção inválida!')

print(f'O resultado é {resultado}')