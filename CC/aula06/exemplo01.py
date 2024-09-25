from time import sleep

def enviar_lembrete():
    # Variável de controle
    spam = 0

    while spam < 5:
        spam = spam + 1
        print(f'Altere sua senha. Lembrete n {spam}')
        
        # spam += 1
        sleep(2)


if __name__ == '__main__':

    enviar_lembrete()