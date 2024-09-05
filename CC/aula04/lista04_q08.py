# Contexto: Um programa de descontos em uma loja. 
# Questão: Escreva um programa que dê descontos de acordo 
# com o valor da compra: acima de R$100, desconto de 10%; 
# entre R$50 e R$100, desconto de 5%; abaixo de R$50, 
# sem desconto. Calcule e mostre o valor do desconto e o 
# valor total a pagar.

valor_da_compra = 100.00

if valor_da_compra >= 100.00:
    
    desconto = valor_da_compra * 0.1
    print(f'Valor R$ {valor_da_compra - desconto} | Desconto: {desconto}')

elif 50 <= valor_da_compra < 100.00:
    
    desconto = valor_da_compra * 0.05
    print(f'Valor R$ {valor_da_compra - desconto} | Desconto: {desconto}')

else:
    print(f'Valor R$ {valor_da_compra} | Sem desconto!')