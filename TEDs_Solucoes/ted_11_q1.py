# -*- coding: utf-8 -*-
"""
Created on Sun May  1 11:36:12 2022

@author: mrafa



Construa uma matriz A de tamanho 10 x 10 com valores inteiros e randômicos.
Depois:

 Imprima o resultado da soma de todos os valores da matriz no terminal;

 E, criei uma nova matriz B, no qual cada item seja o valor da matriz A * 3;

"""

# Importação das bibliotecas
import random


# Criando nossa matriz vazia
matriz_a = []


# Criando a matriz com uma matriz_auxiliar
for i in range(10):
    
    matriz_aux = []
    
    for j in range(10):    
        matriz_aux.append(random.randint(0, 100))
    
    matriz_a.append(matriz_aux)        

# Imprimindo a matriz para verificação
for linha in matriz_a:
    print(linha)
    
print('\n \n')
    
# Somando todos os valores da Matriz

resultado_soma = 0

for l in matriz_a:
    
    for c in l:
        
        resultado_soma += c

print(f'Resultado da Soma = {resultado_soma}')

matriz_b = []

for l in range(0, len(matriz_a)):
    
    lista_auxiliar = []
    
    for c in range(0, len(matriz_a[l])):
        
        resultado_multiplicacao = matriz_a[l][c] * 3
        lista_auxiliar.append(resultado_multiplicacao)
        
    matriz_b.append(lista_auxiliar)
        
print(matriz_b)





