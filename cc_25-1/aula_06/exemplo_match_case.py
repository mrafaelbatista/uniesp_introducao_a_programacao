dia = int(input('Digite um dia numérico: '))

match dia:
    case 1:
        print("Dia útil!")
    case 2:
        print("Final de semana ou feriado!")
    case 3:
        print('Bad day!!!')
    case _:
        print(f"Valor {dia} inválido")