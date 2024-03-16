'''
Armazene os nomes de alguns de seus amigos em uma
lista chamada amigos. Exiba o nome de cada pessoa
acessando cada elemento da lista um de cada vez.
'''

lista_amigos = [
    'Analicia',
    'Luiz',
    'Galvão Bueno',
    'João']

# for nome in lista_amigos:
#     print(f'{nome}, obrigado por vir a aula!')

x = 0
while x < len(lista_amigos):
    print(f'{lista_amigos[x]}, obrigado por vir a aula!')
    x += 1
