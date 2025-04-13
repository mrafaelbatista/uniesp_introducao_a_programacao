qtd_max = 1000
qtd_min = 10
qtd = 100

media_estoque = (qtd_max + qtd_min) / 2

if qtd >= media_estoque:
    print('Não efetuar a compra!')

elif qtd < media_estoque:
    print('Efetuar a compra!')