valor_da_compra = float(input('Digite o valor da nota: '))

if valor_da_compra > 100:
    valor_da_compra -= (valor_da_compra * 0.1)

elif 50 <= valor_da_compra <= 100:
    valor_da_compra = valor_da_compra - (valor_da_compra * 0.05)

elif valor_da_compra < 50:
    valor_da_compra = valor_da_compra

print(f'O valor total a pagar é de R$ {valor_da_compra}')
