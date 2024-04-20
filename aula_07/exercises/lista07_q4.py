# Ler um vetor A de 10 números. Após, ler mais um número e
# guardar em uma variável x. Armazenar em um vetor M o resultado
# de cada elemento de A multiplicado pelo valor X. Logo após,
# imprimir o vetor M.
from random import randint

vet_a = []
vet_m = []
multiplicador_x = 5

for n in range(10):
    vet_a.append(randint(0, 10))

for posicao in range(len(vet_a)):
    resultado = vet_a[posicao] * multiplicador_x
    vet_m.append(resultado)

print('Vetor A: ')
print(vet_a)
print('Vetor M:')
print(vet_m)
