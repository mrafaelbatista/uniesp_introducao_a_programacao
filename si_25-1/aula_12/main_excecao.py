lista = [1, 0 , 9]

try:
    print(lista[99])

except Exception as e:
    print(f'Erro: {e}')

print('Fim do programa!')