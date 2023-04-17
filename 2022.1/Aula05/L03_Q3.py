# Crie um programa em Python que solicite um número
# do usuário, depois some este número com 1357,
# multiplique por 8, divida por 5 e eleve ao quadrado.

# Resolução da questão (Forma 1)
numero = int(input("Digite um número: "))

# Cálculos da questão realizados por parte
numero = numero + 1357
numero = numero * 8
numero = numero / 5
numero = numero ** 2

# Mesma questão (forma 2)
num = int(input("Digite outro número: "))

# Expressão matemática com todos os cálculos (resumido)
resultado = ((((num + 1357) * 8) / 5) ** 2)

# Formatando a saída de dados (forma 1)
print(f"{resultado :.2f}")

# Formatando a saída de dados (forma 2)
print("%0.5f" % (resultado))


'''Método de String upper(), transforma a string
em um texto em caixa alta.'''
print("Messias".upper())

'''Utilizando o método upper() no retorno do input'''
nome = input("Digite seu nome: ").upper()
print(f'Seu nome {nome}, é legal!')