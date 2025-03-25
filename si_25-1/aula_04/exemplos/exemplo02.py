nota = float(input('Digite sua nota: '))

if nota >= 7:
    if 7 <= nota <= 8:
        print('Você foi bem!')
    elif 8 < nota < 9:
        print('Você foi muito bem!')
    else:
        print('Você foi excelente!')
else:
    print('É preciso estudar um pouco mais!')