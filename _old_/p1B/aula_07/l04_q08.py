hora_extra = int(input('Horas-extras: '))
hora_ausente = int(input('Horas ausentes: '))

horas_ausentes_50 = (hora_ausente * 1.5)

if hora_extra > horas_ausentes_50:
    print('Bônus de R$ 500,00')
else:
    print('Sem bônus!')
