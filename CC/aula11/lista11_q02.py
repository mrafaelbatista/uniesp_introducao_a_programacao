lista_de_notas = [8, 10, 5.6, 7, 4.8]

# media soma dos itens / quantidade dos itens
soma = 0

# Acumular os valores na variável soma
for i in range(len(lista_de_notas)):
    soma += lista_de_notas[i]

# Pergunta: qual a média da turma?
media = soma / len(lista_de_notas)

contadora = 0

# Pergunta 2: quantos alunos acima da média?
for i in range(len(lista_de_notas)):
    if lista_de_notas[i] > media:
        contadora += 1

print(f'A média da turma é: {media:.2f}')
print(f'{contadora} alunos acima da média.')