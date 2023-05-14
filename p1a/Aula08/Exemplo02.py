frutas = ['pêra', 'uva', 'maçã', 'kiwi']
print(frutas)
frutas[1] = 'abacate'
print(frutas)
frutas.insert(2, 'morango')
print(frutas)
frutas.insert(10, 'xcvbnm')
print(frutas)
del frutas[5]
print(frutas)
frutas.append('melancia')
print(frutas)
del frutas[frutas.index('melancia')]
print(frutas)
frutas.remove('maçã')
print(frutas)
frutas.append('abacaxi')
print(frutas)
pop_frutas = frutas.pop(frutas.index('abacaxi'))
print(frutas)
print(f'A fruta {pop_frutas} foi deletada.')