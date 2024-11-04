# Programa: Lista de Compras
lista_de_compras = []

op = -1

while op != 0:
    print('1 - Adicionar novo item')
    print('2 - Remover item')
    print('3 - Exibir lista completa')
    print('0 - Sair do programa')
    op = int(input('Digite a opção desejada: '))

    if op == 1:
        print('\n')
        print('====> Adicionar item <====')
        item = input('Digite o item desejado: ')
        
        lista_de_compras = lista_de_compras + [item]

        print(f'O item {item} foi adicionado a lista de compras.')

    elif op == 2:
        print('\n')
        print('====> Exibir lista <====')

        for i in range(len(lista_de_compras)):
            print(f'{i+1} | {lista_de_compras[i]}')

        print('----------------------------------')

        item = int(input('Digite o código do item a ser removido: '))
        item_deletado = lista_de_compras[item-1]
        
        del lista_de_compras[item-1]

        print(f'O item {item_deletado} foi removido da lista.')

        print('----------------------------------')

    elif op == 3:
        print('\n')
        print('====> Exibir lista <====')

        for i in range(len(lista_de_compras)):
            print(f'{i+1} | {lista_de_compras[i]}')

        print('----------------------------------')

    elif op == 0:
        print('====> Programa finalizado <====')
    else:
        print(':::: Opção inválida! ::::')