valor_da_compra = float(input('Qual o valor da compra:'))

if valor_da_compra > 100:
    desconto = valor_da_compra * 0.1
    print(f'Valor: R${(valor_da_compra - desconto)}')
    print(f'Desconto: R${desconto}')

elif 50 <= valor_da_compra <= 100:
    desconto = valor_da_compra * 0.05
    print(f'Valor: R${(valor_da_compra - desconto)}')
    print(f'Desconto: R${desconto}')

else:
    print(f'Valor: R${valor_da_compra}')
