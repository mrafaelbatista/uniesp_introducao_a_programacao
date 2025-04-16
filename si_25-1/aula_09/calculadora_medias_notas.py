controle = True
notas = []

while controle:
    print('Digite 100 para SAIR')
    print('ou digite a nota desejada!')

    nota = int(input('Digite a nota: '))

    if 0 <= nota <= 10:
        notas.append(nota)

    elif nota == 100:
        controle = False
    else:
        print('Valor inválido!')

print('As notas são: ')
print(notas)