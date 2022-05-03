# -*- coding: utf-8 -*-
"""
Created on Mon May  2 20:53:20 2022

@author: mrafa

Questão 08
Faça um cadastro de usuários com nome, idade e email,
utilizando apenas o que você aprendeu até agora.

"""
controle = 1
cadastros = []

while controle != 0:
    
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")
    controle = int(input("Digite a opção: "))
    
    # Cadastro
    if controle == 1:
        
        pessoa = []
        
        nome = input("Digite o nome da pessoa: ")
        pessoa.append(nome)
        
        email = input("Digite o e-mail: ")
        pessoa.append(email)
        
        idade = int(input("Digite a idade: "))
        pessoa.append(idade)
        
        cadastros.append(pessoa)
        
        
    # Listar pessoas cadastradas
    elif controle == 2:
        
        if cadastros is None:
            
            print("Não temos registros")
        
        else:
            
            for p in cadastros:
                
                print(p)
    
    elif controle == 0:
        
        print("Obrigado! Gostei de interagir com você :\)")
        
