'''Faça um algoritmo para ler 20 números e armazenar em um vetor.
Após a leitura total dos 20 números, o algoritmo deve escrever 
esses 20 números lidos na ordem inversa.'''

# Importações das bibliotecas
import random

# Criando a lista que vai armazenar os 20 números
lista_de_numeros = []

# Estrutura de repetição for
for n in range(0, 20):
    # Adicionando números randômicos na lista
    lista_de_numeros.append(random.randint(0, 1000))
    
print(f'Lista de Números: {lista_de_numeros}')

# Solução 2 - Moderado | Recomendada pois trabalha os conceitos
# de algoritmos e lógica de programação

# Primeiro vamos descobrir quem é o maior valor

for i in range(0, len(lista_de_numeros)):
    # print(f'----- Iniciando um ciclo de i com valor: {i} -----')
    
    maior_numero = lista_de_numeros[i]
    maior_indice = i
    
    for j in range((i+1), len(lista_de_numeros)):
        
        if lista_de_numeros[j] >= maior_numero:
            maior_numero = lista_de_numeros[j]
            maior_indice = j
            
            # print(f'Valor atualizado - Maior Número: {maior_numero}')
            
    lista_de_numeros.insert(i, lista_de_numeros.pop(maior_indice))
            
    
   
print(lista_de_numeros)