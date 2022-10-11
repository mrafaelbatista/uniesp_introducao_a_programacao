# Exemplo do While

'''Variável de controle, será utilizada para
controlar a quantidade de repetições'''
controle = 1

'''Estrutura do While com expressão lógica.
Esta execução terá 10 repetições e em cada uma
ela irá imprimir o valor presente na variável
controle e incrmentará mais 1 a ela.'''
while controle <= 10:
    print(controle)
    controle += 1

# Exemplo do For
'''A função range segue com três argumentos,
o primeiro 1, refere-se ao valor inicial, o 11,
é o valor final não inclusivo, e por fim 1, que
é o incremento'''
for i in range(1, 11, 1):
    print(i)
