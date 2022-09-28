cadastros = []

botao = 1000
while botao != 0:
    # teste comite
    print("Digite 1 para cadastrar um novo usuário")
    print("Digite 2 para imprimir todos os usuários")
    print("Digite 0 para sair")
    botao = int(input("Digite a opção desejada: "))

    if botao == 1:
        # Entrada dos dados
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        email = input("Digite o e-mail: ")
        # Folha de Cadastro
        dados = [nome, idade, email]
        # Guardando a folha na pasta
        cadastros.append(dados)

    elif botao == 2:
        
        for p in cadastros:
            print(p)

    elif botao == 0:
        print("Obrigado por acessar este software!")

    else:
        print("Digite um número válido!")