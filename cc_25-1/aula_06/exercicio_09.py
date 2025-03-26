nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2) / 2

if media >= 6.0:
    print(f'Aluno aprovado com média {media}')
else:
    print(f'Aluno reprovado com média {media}')