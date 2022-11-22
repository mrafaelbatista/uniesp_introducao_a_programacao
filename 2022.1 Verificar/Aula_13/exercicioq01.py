'''
Use um dicionário para armazenar informações sobre uma pessoa
que você conheça. Armazene seu primeiro nome, o sobrenome,
a idade e a cidade em que ela vive. Você deverá ter chaves
como primeiro_nome, sobrenome, idade, e cidade. Por fim, mostre
cada informação armazenada em seu dicionário.
'''

cadastros = {
    'Samuel' : {'nome':'Samuel Alves', 'idade': 21, 'cidade':'Timbaúba-PE'},
    'Praxedes' : {'nome':'Jardel Praxedes', 'idade': 21, 'cidade':'Lucena-PB'},
    'Gustavo' : {'nome':'Gustavo Lindão', 'idade': 18, 'cidade':'João Pessoa-PB'}
}

for i in cadastros:
    nome = cadastros[i]['nome']
    idade = cadastros[i]['idade']
    print(f'O nome é {nome} e sua idade é {idade}')

cadastros['Samuel']['idade']