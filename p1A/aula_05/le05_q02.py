# Faça um programa que mostre as tabuadas
# dos números de 1 a 10.

# for i in range(1, 11):
#      for j in range(1, 11):
#          print(f' {i} x {j} = {(i*j)}')
#
num1 = 1
while num1 <= 10:
    num2 = 1
    while num2 <= 10:
        print(f'{num1} + {num2} = {(num1 + num2)}')
        num2 += 1
    num1 += 1

