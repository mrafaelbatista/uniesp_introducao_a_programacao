# Crie um programa em Python que pergunte o
# nome do usuário e imprima um bom dia com
# o nome do usuário. Dica: você pode utilizar
# o método .format() ou uma concatenação de
# string, por exemplo.

# Input para solicitar o nome do usuário
nome = input("Digite o seu nome: ")

# Imprimir na tela utilizando o método .format
print("Bom dia, {}".format(nome))

# Concatenando o texto bom dia com o nome
mensagem = "Bom dia, " + nome

# Imprimindo o valor da variável mensagem
print(mensagem)
