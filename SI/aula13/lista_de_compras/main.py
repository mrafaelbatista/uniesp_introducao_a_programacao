lista_de_compras = []

# Opção 1
def adicionar_item(lista_de_compras:list) -> list:
    novo_item = input('Digite o novo item a ser adicionado: ')
    lista_de_compras = lista_de_compras + [novo_item]

    return lista_de_compras


# Opção 2
def deletar_item(lista_de_compras:list) -> list:
    
    item_remover = int(input('Digite o código do item: ')) - 1
    del lista_de_compras[item_remover]

    return lista_de_compras


# Opção 3
def exibir_lista(lista_de_compras:list):

    for i in range(len(lista_de_compras)):
        print(f'{i+1} - {lista_de_compras[i]}')

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

       lista_de_compras = adicionar_item(lista_de_compras=lista_de_compras)
       
    
    # Remover item
    elif opcao == 2:
        print('\n====> REMOVER ITEM DA LISTA <====\n')
        
        exibir_lista(lista_de_compras=lista_de_compras)

        print('\n ===')

        lista_de_compras = deletar_item(lista_de_compras=lista_de_compras)
        


    # Exibir a lista completa
    elif opcao == 3:
        print('\n====> LISTA COMPLETA <====\n')

        exibir_lista(lista_de_compras=lista_de_compras)
