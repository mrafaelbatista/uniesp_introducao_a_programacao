# Desenvolva um programa que verifique e mostre
# os números entre 1.000 e 2.000 que, quando
# divididos por 11, produzam o resto igual a 5.

# Solução em for
for num in range(1000, 2001):
    if (num % 11) == 5:
        print(num)

# Solução com While
numero = 1000
while numero <= 2000:
    if (numero % 11) == 5:
        print(f'Este número é legal: {numero}')
    numero += 1