def classifica_plantas_magicas(altura_planta):

    if altura_planta < 1:
        print('Planta pequena')
    
    elif 1 <= altura_planta <= 3:
        print('Planta média')
    
    else:
        print('Planta grande')


if __name__ == '__main__':

    # Coleta a altura da planta
    tamanho_planta = int(input('Digite a altura da planta em mt: '))
    
    # Classifica a platan pela sua altura
    classifica_plantas_magicas(tamanho_planta)
