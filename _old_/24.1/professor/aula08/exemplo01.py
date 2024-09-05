# Lista de alunos e suas notas em diferentes disciplinas
alunos = [["João", [8, 7, 6]], ["Maria", [9, 8, 10]], ["Pedro", [7, 8, 7]]]

# Cálculo da média de cada aluno
for aluno in alunos:
    nome = aluno[0]
    notas = aluno[1]
    media = sum(notas) / len(notas)
    print(f"Média de {nome}: {media}")
