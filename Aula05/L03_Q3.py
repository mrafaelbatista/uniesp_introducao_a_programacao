# Crie um programa em Python que solicite um número
# do usuário, depois some este número com 1357,
# multiplique por 8, divida por 5 e eleve ao quadrado.

numero = int(input("Digite um número: "))

numero = numero + 1357
print(numero)
numero = numero * 8
print(numero)
numero = numero / 5
print(numero)
numero = numero ** 2
print(numero)

num = int(input("Digite outro número: "))
resultado = ((((num + 1357) * 8) / 5) ** 2)

print(f"{resultado :.2f}")
print("%0.5f" % (resultado))
0

# print("Messias")
# print("Messias".upper())

# nome = input("Digite seu nome: ").upper()

# print(f'Seu nome {nome}, é legal!')