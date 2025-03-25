def soma(a, b):
    return a + b


if __name__ == "__main__":
    # Executa os testes
    # Teste com números positivos
    assert soma(1, 2) == 3, "Erro: 1 + 2 deveria ser 3"
    # Teste com números negativos
    assert soma(-1, -2) == -3, "Erro: -1 + -2 deveria ser -3"
    # Teste com zero
    assert soma(0, 0) == 0, "Erro: 0 + 0 deveria ser 0"
    # Teste com números mistos
    assert soma(-1, 1) == 0, "Erro: -1 + 1 deveria ser 0"
    # Teste com números decimais
    assert soma(1.5, 2.5) == 4.0, "Erro: 1.5 + 2.5 deveria ser 4.0"
    assert soma(10, 2.5) == 4.0, "Erro: 1.5 + 2.5 deveria ser 4.0"
