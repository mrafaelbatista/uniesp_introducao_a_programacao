status = True
vingadores = []

def adicionar_vingador():
    vingador = input('Digite o nome do vingador: ')
    vingadores.append(vingador)
    print("------- Vingador Adicionado -------")


def listar_vingadores():
    print("------- Lista dos Vingadores -------")
    tamanho_da_lista = len(vingadores)
    for i in range(tamanho_da_lista):
        print(f'{i} - {vingadores[i]}')
    print("------- Fim da Lista dos Vingadores -------")


def alterar_vingador():
    listar_vingadores()
    n_vingador = int(input('Escolhar o vingador a ser alterado: '))
    vingadores[n_vingador] = input('Digite o novo nome do Vingador: ')
    print("------- Fim da Alteração do Vingador -------")


while status:
    print('0 - Sair')
    print('1 - Adicionar Vingador')
    print('2 - Listar Vingadores')
    print('3 - Alterar Vingador')
    op = int(input('Digite a opção desejada: '))

    if op == 0:
        break
    elif op == 1:
        adicionar_vingador()
    elif op == 2:
        listar_vingadores()
    elif op == 3:
        alterar_vingador()
    else:
        print('Digite uma opção válida!')
