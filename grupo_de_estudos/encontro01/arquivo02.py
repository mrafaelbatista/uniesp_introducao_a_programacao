# Encontrar um valor dentro de um vetor

vet_clubes = [
    'real Madrid',
    'barceLona',
    'Ibis',
    'Manchester United',
    'Paris Saint-German'
]

busca = False # controle

clube_buscado = input('Digite o clube: ').upper()

for i in range(len(vet_clubes)):

    if clube_buscado == vet_clubes[i].upper():
        busca = True

if busca:
    print('Achei')
else:
    print('Não achei!')




