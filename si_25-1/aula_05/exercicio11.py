quant_max = 1000
quant_min = 100

quant_real = 497

quant_media = (quant_max + quant_min) / 2

if quant_real < quant_media:
    print('Realize uma compra para o estoque!')
else:
    print('Não é necessária uma compra!')