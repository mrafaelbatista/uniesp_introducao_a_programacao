# Problema: As maçãs custam R$ 1,30 cada, se forem compradas menos de uma dúzia,
# e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o
# número de maçãs compradas, calcule e escreva o custo total da compra.

quantidade = int(input('Digite a quantidade de maçãs desejadas: '))

if 0 < quantidade < 12:
    total = quantidade * 1.30
else:
    total = quantidade * 1

print(f'O valor para {quantidade} maçãs é de R$ {total}.')
