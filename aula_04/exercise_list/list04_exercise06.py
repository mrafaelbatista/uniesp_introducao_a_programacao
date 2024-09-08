saldo = 1000
debito = 800
credito = 500

saldo = saldo - debito + credito
print(f'Saldo atual: {saldo}')

if saldo >= 0:
    print('Saldo positivo')
else:
    print('Saldo negativo')