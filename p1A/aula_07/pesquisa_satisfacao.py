from random import randint

# Constante número de funcionários
QTD_CLI = 100

lista_respostas = []

for i in range(QTD_CLI):
    lista_respostas.append(randint(1, 5))

print(f'Qtd com (1) - {lista_respostas.count(1)}')
print(f'Qtd com (2) - {lista_respostas.count(2)}')
print(f'Qtd com (3) - {lista_respostas.count(3)}')
print(f'Qtd com (4) - {lista_respostas.count(4)}')
print(f'Qtd com (5) - {lista_respostas.count(5)}')
