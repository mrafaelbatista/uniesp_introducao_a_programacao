lista_de_compras = []

opcao = 1000

while opcao != 0:
    print('\n =======================')
    print('1 - Adicionar novo item')
    print('2 - Remover item')
    print('3 - Exibir lista completa')
    print('0 - Sair')
    opcao = int(input('Digite a opção desejada: '))

    # Criar opção para adicionar novo item a lista
    if opcao == 1:
       print('\n====> ADICIONAR ITEM <====\n')
       
       novo_item = input('Digite o novo item a ser adicionado: ')
       lista_de_compras = lista_de_compras + [novo_item]
    
    # Remover item
    elif opcao == 2:
        print('\n====> REMOVER ITEM DA LISTA <====\n')
        
        for i in range(len(lista_de_compras)):
            print(f'{i+1} - {lista_de_compras[i]}')

        print('\n ===')

        item_remover = int(input('Digite o código do item: ')) - 1[]
        
        del lista_de_compras[item_remover]


    # Exibir a lista completa
    elif opcao == 3:
        print('\n====> LISTA COMPLETA <====\n')

        for i in range(len(lista_de_compras)):
            print(f'{i+1} - {lista_de_compras[i]}')