estoque = [["Camiseta", 25.99, 10],
             ["Calça", 59.99, 5],
             ["Tênis", 99.99, 3],
             ["Boné", 15.99, 20]]

for produto in estoque:
    print('---------')
    print(f'Produto: {produto[0]} | R$ {produto[1]} | Quant: {produto[2]}')

    