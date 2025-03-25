# 01 dados de entrada
n_conta = input('Digite o número da conta: ')
saldo_ini = float(input('Digite o seu saldo: '))
debito = float(input('Digite o valor desejado: '))
credito = float(input('Digite o crédito: '))

# 02 processamento
print(f'O saldo atual é R${saldo_ini}.')

saldo = saldo_ini - debito + credito

# 03 saída
if saldo >= 0:
    print(f'O saldo R${saldo} é positivo!')
else:
    print(f'O saldo R${saldo} é negativo!')
