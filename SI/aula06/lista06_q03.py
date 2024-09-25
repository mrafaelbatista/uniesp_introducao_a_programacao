from time import sleep

def tabuada(numero):

    for m in range(1, 11, 1):
        print(f'{numero} x {m} = {numero*m}')
        sleep(1)

if __name__ == '__main__':

    numero = int(input('Digite um número: '))
    tabuada(numero)