numero = int(input('Digite o número da tabuada: '))

print('---- Solução com FOR ----')
for m in range(1, 11):
    resultado = numero * m
    print(f'{numero} x {m} = {resultado}')

print('---- Solução com WHILE ----')
ciclos = 1

while ciclos <= 10:
    resultado = numero * ciclos
    print(f'{numero} x {ciclos} = {resultado}')
    # Incremento
    ciclos += 1
