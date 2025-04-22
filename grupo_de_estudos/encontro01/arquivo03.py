vet_clubes = [
    'real Madrid'.upper(),
    'barceLona'.upper(),
    'Ibis'.upper(),
    'Manchester United'.upper(),
    'Paris Saint-German'.upper()
]

clube_buscado = input('Digite o clube: ').upper()

if clube_buscado in vet_clubes:
    print('Achei')
else:
    print('Não achei!')