# Lendo duas notas de avaliação
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Cálculo da média aritmética
media = (nota1 + nota2) / 2

if 6 <= media <= 10:
    print(f'Aluno APROVADO com média {media}.')
elif 0 <= media < 6:
    print(f'Aluno REPROVADO com média {media}.')
else:
    print(f'Valor da média inválido -> {media}')