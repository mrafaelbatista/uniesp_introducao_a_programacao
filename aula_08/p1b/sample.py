status = True
vingadores = []

def adicionar_vingador():
    vingador = input('Digite o nome do vingador: ')
    vingadores.append(vingador)
    print("------- Vingador Adicionado -------")


def listar_vingadores():
    print("------- Lista dos Vingadores -------")
    for v in vingadores:
        print(v)

    print("------- Fim da Lista dos Vingadores -------")


while status:
    print('0 - Sair')
    print('1 - Adicionar Vingador')
    print('2 - Listar Vingadores')
    op = int(input('Digite a opção desejada: '))

    if op == 0:
        break
    elif op == 1:
        adicionar_vingador()
    elif op == 2:
        listar_vingadores()
    else:
        print('Digite uma opção válida!')
