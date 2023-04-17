qtd_max = 10000
qtd_min = 1000
qtd_prod = 5456

media_prod = (qtd_max + qtd_min) / 2

if qtd_prod > media_prod:
    print("Não precisa comprar!")
else:
    print("Efetuar a compra!")