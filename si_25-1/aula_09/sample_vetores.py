jogos = [
    'Pokemon Go',
    'Super Mario',
    'Sonic',
    'Super Star Soccer Deluxe',
    'Alien'
]

# Imprimindo toda a lista
print(jogos)

# Imprimindo apenas o Sonic
print(jogos[2])

# Desafio
# Crie um programa para imprimir cada jogo
# Com uma mensagem que o jogo é legal!

# Utilizando lista
for jogo in jogos:
    print(f'O jogo {jogo} é muito arretado!')

print('---------------')

print(f'O tamanho da lista jogos é {len(jogos)}')

# Utilizando o conceito de vetor
for i in range(len(jogos)):
    print(f'[{i+1}] O jogo arretado é: {jogos[i]}')