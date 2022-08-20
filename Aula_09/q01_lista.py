""" Desenvolva um programa que verifique e mostre os números entre 1.000 e 2.000 que,
quando divididos por 11, produzam o resto igual a 5. """

for i in range(1000, 2001):
    if (i % 11) == 5:
        print(i)