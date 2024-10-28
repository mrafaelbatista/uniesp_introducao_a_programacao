# Escreva um algoritmo que permita a leitura dos nomes de 5 clubes de futebol
# e armazene os nomes idos em um vetor. Após isto, o algoritmo deve permitir
# a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem
# ACHEI, se o nome estiver entre os 5 nomes lidos anteriormente (guardados no
# vetor), ou NÃO ACHEI caso contrário.

clubes = ['Ibis', 'Araruna', 'Serra Branca', 'Tubarão', 'Sport de Cacimba']

clube_verificador = input('Digite o seu clube do coração: ')

confirmacao_de_busca = False


for clube in clubes:

    if clube.upper() == clube_verificador.upper():
        confirmacao_de_busca = True

if confirmacao_de_busca:
    print('Achei!')
else:
    print('Não achei!')



