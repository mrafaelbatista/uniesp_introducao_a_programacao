# Soma de Vetores: Dados dois vetores representados como
# listas em Python, escreva um programa que calcule a soma
# desses vetores e exiba o resultado.

vet_a = [1, 2, 3, 4, 5]
vet_b = [9, 8, 7, 6, 5]

vet_c = []

for i in range(len(vet_a)):
    soma = vet_a[i] + vet_b[i]
    vet_c.append(soma)

print(vet_c)

