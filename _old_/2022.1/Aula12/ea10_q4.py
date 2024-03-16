from random import randint

lista_num = []
nova_lista = []

for i in range(10):
    lista_num.append(randint(0, 100))

x = randint(0,9)

for i in range(len(lista_num)):
    nova_lista.append(x * lista_num[i])

print(lista_num)
print(x)
print(nova_lista)
