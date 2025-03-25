media = float(input('Digite sua média final: '))

if media >= 7.0:
    if media > 9.0:
        print('Excelente! Você é arretado!')
    elif 8.0 < media <= 9.0:
        print('Foi de boa!!!')
    elif 7.0 <= media <= 8.0:
        print('Passou e quase que se lasca!!!')
else:
    print('Reprovado!')