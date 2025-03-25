# Programa: Lista de Compras
lista_de_compras = [] # variável global
op = -1


# Opção 01 - Adicioner item a lista
def adicionar_item(lista_compras:list) -> list:
    print('\n')
    print('====> Adicionar item <====')
    item = input('Digite o item desejado: ')
    
    lista_compras = lista_compras + [item]

    print(f'O item {item} foi adicionado a lista de compras.')

    return lista_compras


# Opção 02 - Remover da lista
def remover_da_lista(lista_compras:list) -> list:

    item = int(input('Digite o código do item a ser removido: '))
    item_deletado = lista_compras[item-1]
    
    del lista_compras[item-1]

    print(f'O item {item_deletado} foi removido da lista.')

    print('----------------------------------')

    return lista_compras


# Opção 03 - Exibir a lista
def exibir_lista(lista_compras:list):
    
    print('\n')
    print('====> --- Exibir lista --- <====')

    for i in range(len(lista_compras)):
        print(f'{i+1} | {lista_compras[i]}')

    print('----------------------------------')


while op != 0:
    print('1 - Adicionar novo item')
    print('2 - Remover item')
    print('3 - Exibir lista completa')
    print('0 - Sair do programa')
    op = int(input('Digite a opção desejada: '))

    if op == 1:
        lista_de_compras = adicionar_item(lista_compras=lista_de_compras)

    elif op == 2:
        exibir_lista(lista_compras=lista_de_compras)
        lista_de_compras = remover_da_lista(lista_compras=lista_de_compras)

    elif op == 3:
        exibir_lista(lista_compras=lista_de_compras)

    elif op == 0:
        print('====> Programa finalizado <====')
    else:
        print(':::: Opção inválida! ::::')