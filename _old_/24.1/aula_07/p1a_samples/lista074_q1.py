alunos = [
    ["João", [8, 7, 6]],
    ["Maria", [9, 8, 10]],
    ["Pedro", [7, 8, 7]],
    ["Ana", [6, 5, 8]],
    ["Carlos", [9, 9, 9]],
    ["Mariana", [7, 8, 7]],
    ["José", [10, 9, 8]],
    ["Sofia", [6, 7, 6]],
    ["Rafael", [8, 8, 7]],
    ["Camila", [9, 9, 10]],
    ["Felipe", [7, 6, 7]],
    ["Patrícia", [8, 8, 9]],
    ["Lucas", [9, 10, 9]],
    ["Juliana", [6, 7, 6]],
    ["Paulo", [8, 8, 7]],
    ["Fernanda", [9, 9, 10]],
    ["Gustavo", [7, 6, 7]],
    ["Larissa", [8, 8, 9]],
    ["Mateus", [9, 10, 9]],
    ["Carolina", [6, 7, 6]]
]

for posicao in range(len(alunos)):
    nome = alunos[posicao][0]
    soma = 0
    
    for indice in range(len(alunos[posicao][1])):
        soma = soma + alunos[posicao][1][indice]

    media = soma / len(alunos[posicao][1])

    print(f'Aluno: {nome} | Média: {media}')