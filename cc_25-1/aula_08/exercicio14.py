import time

for num in range(1000, 2001):
    if num % 11 == 5:
        print(f'O número é {num}.')
        time.sleep(1)

numero = 1000

while numero <= 2000:
    if numero % 11 == 5:
        print(f'O número é {numero}.')

    # numero = numero + 1
    numero += 1