lista_de_melhores_clubes = []

controle = 0

while True:

    print('1 - Inserir Clube')
    print('2 - Sair do Programa')
    print('3 - Imprimir a lista')

    controle = int(input('Digite sua opção: '))

    if controle == 1:

        clube = input('Digite nome do clube: ')
        lista_de_melhores_clubes.append(clube)

    elif controle == 2:
        break

    elif controle == 3:
        print(lista_de_melhores_clubes)


print('Parou o programa!')
