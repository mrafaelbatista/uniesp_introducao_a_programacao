lista_exemplo = ['a', 'b']
try:
    solucao = 50/2 #50/0
    solucao2 = lista_exemplo[10]

except ZeroDivisionError as e:
    print(f'Error: Usuário você teve uma erro -> {e}')

except IndexError as e:
    print(f'Error diferente: {e}')

else:
    print(f'Solução: {solucao}')
    print(f'Solução2: {solucao2}')
