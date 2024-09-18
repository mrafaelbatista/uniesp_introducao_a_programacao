distancia_dragao1 = float(input("Distância percorrida pelo Dragão 1 (km): "))
tempo_dragao1 = float(input("Tempo do Dragão 1 (horas): "))

distancia_dragao2 = float(input("Distância percorrida pelo Dragão 2 (km): "))
tempo_dragao2 = float(input("Tempo do Dragão 2 (horas): "))

velocidade_dragao1 = distancia_dragao1 / tempo_dragao1
velocidade_dragao2 = distancia_dragao2 / tempo_dragao2

if velocidade_dragao1 > velocidade_dragao2:
    print("Dragão 1 é mais rápido!")
elif velocidade_dragao2 > velocidade_dragao1:
    print("Dragão 2 é mais rápido!")
else:
    print("Ambos os dragões têm a mesma velocidade!")
