# # Declaração de uma lista
# nomes = ['João', 'Yasmin', 'Higor', 'Maria']
# # Impressão da lista
# print(nomes)
# # Impressão do tipo de dados
# print(type(nomes))
# # Tamanho da lista
# print(len(nomes))
# # Imprimir os itens da lista
# print(nomes[0])
# print(nomes[1])
# print(nomes[2])
# print(nomes[3])

frutas = ['pêra', 'uva', 'maçã', 'kiwi']
print(frutas)

frutas[1] = 'abacate'
print(frutas)

frutas.insert(2, 'morango')
print(frutas)
frutas.insert(5, 'Chuchu') #não é fruta
print(frutas)
del frutas[5]
print(frutas)
frutas.insert(5, 'Melancia')
print(frutas)
print(f'O que é o frutas.index {frutas.index("Melancia")}')
del frutas[frutas.index('Melancia')]
print(frutas)
frutas.remove('kiwi')
print(frutas)
frutas.insert(10, 'Ameixa')
print(frutas)
pop_fruta = frutas.pop(frutas.index('Ameixa'))
print(f'Pop Fruta - {pop_fruta}')
print(frutas)
