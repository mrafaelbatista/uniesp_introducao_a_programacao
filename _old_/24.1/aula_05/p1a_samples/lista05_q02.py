# Faça um programa que calcule as tabuadas dos números
# de 1 a 10 e armazene o resultado em um arquivo de texto.

for i in range(1, 11):

    for j in range(1, 11):
        # Adicionando a tabuada ao arquivo de texto
        with open('arquivo.txt', 'a') as file:

            # Escrevendo no arquivo de texto
            file.write(f'{i} x {j} = {i*j}\n')

        # Imprimindo o valor no terminal
        print(f'{i} x {j} = {i*j}')

