from random import randint

v1 = []
v2 = []

for n in range(10):
    v1.append(randint(0, 5))
    v2.append(randint(0, 5))

print(v1)
print(v2)

# Criar a lógica para comparar se um
# número é igual e está na mesma posição

for i in range(len(v1)):
    if v1[i] == v2[i]:
        print(f"O valor {v1[i]} e {v2[i]} são iguais!")
        print(f"Estão os dois na posição {i}")