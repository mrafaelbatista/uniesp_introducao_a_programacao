def convidar_vingador():

    with open('vingadores.txt', 'r', encoding='utf-8') as arquivo:

        for i in arquivo:
            heroi = arquivo.readline()
            print(f'Por favor, venha a minha festa, {heroi}.')


if __name__ == '__main__':
    
    convidar_vingador()