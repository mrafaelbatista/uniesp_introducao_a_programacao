def cast_feitico(feitico):

    match feitico:
        case 1:
            print('Bola de fogo!')
        case 2:
            print('Bola de água!')
        case 3:
            print('Bola de terra!')


if __name__ == '__main__':

    print('1 - Fogo')
    print('2 - Água')
    print('3 - Terra')
    escolha_feitico = int(input('Escolha seu feitiço: '))
    cast_feitico(escolha_feitico)