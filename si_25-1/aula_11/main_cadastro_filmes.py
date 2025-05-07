import time

bd_filmes = [
    ['Interestelar', 2015],
    ['Titanic', 1997],
    ['Star Wars: Episodio 6', 2022]
]

# Listar Filmes
def listar_filmes(bd):
    for i in range(len(bd)):
        print(f'{i+1} - {bd[i][1] } - {bd[i][0]}')


# Cadastrar filmes
def cadastrar_filme(bd, titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd


while True:
    print('Bem-vindo ao CadFilme')
    print('1 - Cadastrar filme')
    print('2 - Alterar filme')
    print('3 - Listar filmes')
    print('0 - Sair')

    try:
        op = int(input('Digite a opção desejada: '))
    except Exception as e:
        print(f'Error: {e}')
        op = -1

    time.sleep(1)

    if op == 1:
        print(f'---- CADASTRO DE FILMES ----')
        titulo = input('Digite o título do novo filme: ')
        ano = int(input('Digite o ano do novo filme: '))
        bd_filmes = cadastrar_filme(
            bd=bd_filmes,
            titulo=titulo,
            ano=ano
        )
        print(f'---- CADASTRO DE FILMES ----')

    elif op == 2:
        print(f'---- ALTERAR FILME ----')
        listar_filmes(bd=bd_filmes)
        i = int(input('Qual filme deseja alterar? '))

        n_titulo = input('Digite o novo título: ')
        n_ano = int(input('Digite o novo ano: '))



        print(f'---- ALTERAR FILME ----')
    elif op == 3:
        print(f'---- LISTAGEM DE FILMES ----')
        listar_filmes(bd=bd_filmes)
        print(f'---- LISTAGEM DE FILMES ----')

    elif op == 0:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida! Tente novamente!')

    time.sleep(2)