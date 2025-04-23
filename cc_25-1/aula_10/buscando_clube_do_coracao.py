# Entrada de Dados
selecoes = [
    'Malásia',
    'China',
    'Gabão',
    'Malta'
]

selecao = input('Digite a seleção desejada: ')
find = False

# Processamento dos dados
for i in range(len(selecoes)):

    if selecao.upper() == selecoes[i].upper():
        find = True

# Saída de Dados
if find:
    print('Achei!')
else:
    print('Não achei!')


