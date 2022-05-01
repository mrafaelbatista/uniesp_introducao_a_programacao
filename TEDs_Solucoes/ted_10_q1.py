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
    lista_de_numeros.append(random.randint(0, 50))
    
print(f'Lista de Números: {lista_de_numeros}')

# Solução 1 - Fácil | Não recomendada nesta disciplina
lista_de_numeros_com_sort = lista_de_numeros.sort(reverse=True)
print(f'Lista de Números ordenados: {lista_de_numeros_com_sort}')

print(lista_de_numeros)

# Solução 2 - Moderado | Recomendada pois trabalha os conceitos
# de algoritmos e lógica de programação

#for numero in lista_de_numeros 