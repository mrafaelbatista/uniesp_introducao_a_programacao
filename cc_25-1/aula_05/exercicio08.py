total_compras = float(input('Digite o valor total: '))
desconto = 0.0

if total_compras > 100:
    desconto = total_compras * 0.9
    print(f'O valor total R$ {desconto} \
            e o desconto de 10%. ')

elif 50 < total_compras <= 100:
    desconto = total_compras * 0.95
    print(f'O valor total R$ {desconto} e o\
            desconto de 5%. ')

elif 0 <= total_compras <= 50:
    print('Você não tem desconto!')
