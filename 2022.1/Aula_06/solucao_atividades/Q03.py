# Crie um programa em Python que solicite
# um número do usuário, depois some este
# número com 1357, multiplique por 8,
# divida por 5 e eleve ao quadrado.

numero = float(input("Digite o número: "))

print("Primeira forma --- Todos os valore separados")
print(numero + 1357)
print(numero * 8)
print(numero / 5)
print(numero ** 2)

print("Segunda forma - Como uma expressão")

resultado = (((numero + 1357) * 8) / 5) ** 2
print(resultado)