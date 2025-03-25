dia = 1

match dia:
    case 1:
        print("Dia útil!")
    case 2:
        print("Final de semana ou feriado!")
    case _:
        print(f"Valor {dia} inválido")