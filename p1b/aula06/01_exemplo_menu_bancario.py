print('Digite uma opção do Menu:')
print('1 - Empréstimos')
print('2 - Financiamentos')
print('3 - Consórcios')

op_menu = int(input('Escolha sua opção: '))

if op_menu == 1:
    print('Você selecionou Empréstimos!')
elif op_menu == 2:
    print('Você selecionou Financiamento!')
elif op_menu == 3:
    print('Você selecionou Consórcios!')
else:
    print('Opção inválida!')