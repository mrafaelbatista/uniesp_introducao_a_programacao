filmes = [
    'Sobreviventes',
    'Pulp Fiction',
    'Up',
    'Sherek',
    'O lobo de Wall Street',
    'Star Trek',
    'Matrix'
]

# Imprimir a lista completa
print(type(filmes))
print(filmes)

# Imprimir apenas um filme
print('--- Imprimindo um filme ---')
print(filmes[1].upper())

# Percorrer a lista de filmes
print('--- Percorrendo uma lista (fácil) ---')
for filme in filmes:
    print(filme.upper())

# Percorrer a lista - Vetor
for i in range(len(filmes)):
    print(filmes[i])


