def calcular_velocidade_dragao(distancia, dragao1, dragao2):

    vel_dga1 = distancia / dragao1
    vel_dga2 = distancia / dragao2

    if vel_dga1 > vel_dga2:
        print('O Banguela (1) é o mais veloz!')
    elif vel_dga2 > vel_dga1:
        print('O Banguela não é o mais veloz!')
    else:
        print('Os dois dragões tem a mesma velocidade!')


if __name__ == '__main__':
    DISTANCIA = 1000

    dragao1 = float(input('Digite o tempo do dragão 1: '))
    dragao2 = float(input('Digite o tempo do dragão 2: '))

    calcular_velocidade_dragao(DISTANCIA, dragao1, dragao2)
