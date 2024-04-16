# Faça um programa que receba um número e que calcule
# a tabuada desse número, e armazene o resultado em
# um arquivo de texto.

numero = int(input('Digite um número: '))

for i in range(1, 11):
    with open('tabuada_q3.txt', 'a') as file:
        file.write(f'{numero} * {i} = {numero*i}\n')