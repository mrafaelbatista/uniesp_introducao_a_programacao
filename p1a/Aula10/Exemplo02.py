# Programa Digite seu nome
# nome = 'x'
#
# while nome != 'seu nome':
#     nome = input('Digite seu nome :')
#     print(f'O nome digitado foi: {nome}')

op = 1000
while op != 0:
    print('1 - Bom dia\n'
          '2 - Boa tarde\n'
          '0 - Sair')
    op = int(input('Digite a operação:'))

    if op == 1:
        print('Bom dia! O sol já nasceu lá na fazendinha!')
    elif op == 2:
        print('Buenas tardes!')
    elif op == 0:
        print('Saindo do programa')
    else:
        print('Valor inválido!')
