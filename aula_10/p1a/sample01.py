lista_zero = [1, 2]

try:
    print(lista_zero[10])
    print(50/0)

except ZeroDivisionError as error:
    print(f'Error da Divisão: {error}')

except IndexError as error:
    print(f'Erro de Index: {error}')

except Exception as error:
    print(f'Outro erro: {error}')

