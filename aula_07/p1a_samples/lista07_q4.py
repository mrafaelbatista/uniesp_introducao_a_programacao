# Ler um vetor A de 10 números. Após, ler mais um número e
# guardar em uma variável x. Armazenar em um vetor M o
# resultado de cada elemento de A multiplicado pelo valor X.
# Logo após, imprimir o vetor M.
from random import randint

vet_a = []

for n in range(10):
    vet_a.append(randint(0, 50))

print(f'Meu vetor -> {vet_a}')

x = 7
vet_b = []

for i in range(len(vet_a)):
    resultado = vet_a[i] * x
    vet_b.append(resultado)

print(f'Vetor B -> {vet_b}')