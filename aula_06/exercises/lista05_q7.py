# Faça um cadastro de usuários com nome, idade e email,
# utilizando apenas o que você aprendeu até agora.

lista = []
op = 1000

while op != 0:
    print('1 - Cadastrar')
    print('0 - Sair')
    op = int(input('Digite a operação: '))

    if op == 1:
        print('--- Cadastro ---')
        nome = input('Digite seu nome: ')
        idade = input('Digite sua idade: ')
        email = input('Digite seu e-mail: ')
        lista.append([nome, idade, email])
vars(322
     32)
for l in lista:
    print(l)