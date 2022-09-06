# -*- coding: utf-8 -*-
"""
Created on Sun May  1 11:19:47 2022

@author: mrafa


Faça um algoritmo para ler 50 números e armazenar em um vetor VET,
verificar e escrever se existem números repetidos no vetor VET e
em que posições se encontram.
"""

# Importações de bibliotecas
import random

# Criando uma variável no contexto do programa
vet = []


# Estrutura de repetição para criar 50 números randomicos
for x in range(50):
    
    vet.append(random.randint(0, 100))

# Imprimindo o vetor para teste
print(f'O vetor criado foi: {vet}')


# Verificar se há número repetidos
for i in range(0, len(vet)):
    
    print(f'VALOR TESTADO: {vet[i]} | ÍNDICE TESTADO: {i}')
    
    for j in range(0, len(vet)):
        
        if vet[i] == vet[j] and i != j:
            print(f'Índice: {j} | Valor: {vet[j]} \n')




