lista = [1, 2, 3]

try:
    print(50/1)
    print(lista[99])

except Exception as e:
    print(f'Erro: {e}')
    print('Informe um divisor válido!')


print('--- fim do programa ---')