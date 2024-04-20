import time

print('--- Iniciando o programa ---')
time.sleep(3)

nota_u1 = float(input('Digite sua primeira nota: '))
nota_u2 = float(input('Digite sua segunda nota: '))

media = (nota_u1 + nota_u2) / 2

# media >= 6 and media <= 10
if 6 <= media <= 10:
    print(f'Parabéns, você foi aprovado, com media {media}!')

# media >= 0 and media < 6
elif 0 <= media < 6:
    print(f'Que pena, você foi reprovado, com media {media}!')

else:
    print('Valores inválidos!')
