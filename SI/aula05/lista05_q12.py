from random import randint

espada_atq = randint(30, 120)
espada_dur = randint(40, 80)

arco_atq = randint(20, 90)
arco_dur = randint(80, 150)

lanca_atq = randint(70, 100)
lanca_dur = randint(30, 120)

if espada_atq > 50 and espada_dur > 70:
    print('Espada')
elif arco_atq > 50 and arco_dur > 70:
    print('Arco')
elif lanca_atq > 50 and lanca_dur > 70:
    print('Lança')
else:
    print('Escolha outra arma!')