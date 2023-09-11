# Questão 08
he = int(input('Digite as horas extras:'))
hf = int(input('Digite as horas faltadas: '))

if he > (hf * 1.5):
    print('Seu bônus é de R$ 500,00')
else:
    print('Sem bônus!')