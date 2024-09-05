lista_ling_prog = []


def adiciona_linguagens(linguagem):
    lista_ling_prog.append(linguagem)
    print('---- Linguagem adicionada com sucesso ----')


def listar_linguagens():
    tamanho_da_lista = len(lista_ling_prog)

    for i in range(tamanho_da_lista):
        print(f'{i} - {lista_ling_prog[i]}')

while True:
    print('0 - Sair')
    print('1 - Adicionar Linguagem')
    print('2 - Listar Linguagens')
    opcao = int(input('Digite sua opção: '))

    if opcao == 0:
        break
    
    elif opcao == 1:
        linguagem = input('Digite a linguagem a ser adicionada: ')
        adiciona_linguagens(linguagem.upper())

    elif opcao == 2:
        listar_linguagens()
        print('---- Linguagens listadas com sucesso ----')
    
    else:
        print('Opção inválida. Tente novamente.')