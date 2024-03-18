qtd_atual = 100
qtd_max = 10000
qtd_min = 50

qtd_media = (qtd_max + qtd_min) / 2

if qtd_atual >= qtd_media:
    print('Não efetuar a compra.')
else:
    print('Efetuar a compra.')
