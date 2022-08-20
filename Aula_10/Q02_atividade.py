# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:12:58 2022

@author: mrafa

Questão 02
Escreva um algoritmo que permita a leitura das notas de uma
turma de 20 alunos. Calcular a média da turma e contar
quantos alunos obtiveram nota acima desta média calculada.
Escrever a média da turma e o resultado da contagem.

"""

notas = [8.0, 7.0, 4.5, 3.2, 3.75, 10.0, 9.0, 8.0, 8.8]

soma = 0
media = 0

for nota in notas:
    
    soma = soma + nota
    
media = soma / len(notas)

contagem_alunos = 0

for n in notas:
    
    if n > media:
        contagem_alunos += 1
        
print('O número de alunos acima da média é {}'.format(contagem_alunos))
        

    

