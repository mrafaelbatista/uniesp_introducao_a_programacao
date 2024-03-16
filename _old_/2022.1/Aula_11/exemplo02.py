import random

m = []

# Criar uma matriz 10 x 10
for x in range(1, 11):
    
    lista_auxiliar = []

    for y in range(1, 11):
        lista_auxiliar.append(random.randint(1, 100000000))

    print("--- Adicionando na Matriz ---")
    print(lista_auxiliar)
    m.append(lista_auxiliar)

print("--- Nossa matriz ---")
print(m)