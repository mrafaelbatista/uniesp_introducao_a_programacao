# Solicita ao usuário que insira o comprimento dos três lados do triângulo
lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))

# Verifica se todos os lados são iguais, indicando um triângulo equilátero
if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")
# Verifica se pelo menos dois lados são iguais, indicando um triângulo isósceles
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles.")
# Se nenhuma das condições anteriores for verdadeira, o triângulo é escaleno
else:
    print("O triângulo é escaleno.")
