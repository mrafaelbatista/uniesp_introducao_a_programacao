''' Exemplo de Dicionário em Python '''

super_hero = {
    'Homem-Aranha': ['Marvel', 'Super massa'],
    'Cleiton Rasta' : 'Brasil',
    'Dr. Estranho' : 'Marvel',
    'Flash' : 'DC',
    'Batman' : 'DC',
    'Homem-formiga' : 'Marvel',
    'Mulher Maravilha' : 'DC'
}

print(super_hero['Homem-Aranha'])
print('\n -------- ')

for i in super_hero:
    print(f'O super hero {i} é da {super_hero[i]}')