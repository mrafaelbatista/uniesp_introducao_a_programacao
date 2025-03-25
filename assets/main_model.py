def exercicio(a, b):
    """Escreva aqui a sua solução"""

    return a + b

if __name__ == '__main__':

    try:
        # Escreva seus testes aqui
        assert exercicio(1, 2) == 3
        assert exercicio(10, 20) == 30

    except Exception as e:
        # Não mexer! Mensagem de erro.
        print(f'Erro: {e}')

    else:
        # Não mexer! Mensagem de sucesso.
        print('Programa executado com sucesso!')