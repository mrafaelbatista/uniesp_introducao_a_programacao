n_conta = 123456
saldo = 1000
debito = 999
credito = 150

saldo_atual = (saldo - debito) + credito

if saldo_atual > 0:
    print(f"O saldo R$ {saldo_atual} é positivo.")
else:
    print(f"O saldo R$ {saldo_atual} é negativo.")