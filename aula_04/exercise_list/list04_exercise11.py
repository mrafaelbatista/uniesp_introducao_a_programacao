# Solicita ao usuário que insira sua idade
idade = int(input("Por favor, informe sua idade: "))

# Verifica a idade e determina o preço do ingresso com base nas condições fornecidas
if idade < 12 or idade > 60:
    preco = 15.00  # Preço do ingresso para pessoas abaixo de 12 anos e acima de 60
else:
    preco = 25.00  # Preço do ingresso para pessoas entre 12 e 60 anos

# Imprime o preço do ingresso
print("O valor do ingresso é R$", preco)
