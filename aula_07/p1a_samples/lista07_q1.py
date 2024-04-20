# Lista de clubes de futebol
clubes = [
    'Vasco',
    'Real Madrid',
    'City',
    'Sousa-PB',
    'Boca',
    'Ibis'
]

# Clube a ser pesquisado
clube_pesquisado = 'Flamengo'
status = False

for posicao in range(len(clubes)):
    if clube_pesquisado == clubes[posicao]:
        status = True

if status:
    print('Achei')
else:
    print('Não achei!')
