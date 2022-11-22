# Crie um programa em Python que solicite
# um número do usuário, depois some este
# número com 1357,
# multiplique por 8,
# divida por 5 e
# eleve ao quadrado.

numero = int(input("Digite um número inteiro: "))

resultado = numero + 1357
resultado = resultado * 8
resultado = resultado / 5
resultado = resultado ** 2

print("O resultado é {}".format(resultado))