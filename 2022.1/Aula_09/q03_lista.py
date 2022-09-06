# -*- coding: utf-8 -*-
"""
Created on Mon May  2 20:43:41 2022

@author: mrafa

Armazene os nomes de alguns de seus amigos em
uma lista chamada amigos. Exiba o nome de cada
pessoa acessando cada elemento da lista um de
cada vez.
"""

amigos = ['Samuel', 'Ryan', 'Alírio']

for i in range(0, len(amigos)):
    
    print(" O nome é: " + amigos[i] + " e tem " \
          + str(len(amigos[i])) + " de letras no nome")
    