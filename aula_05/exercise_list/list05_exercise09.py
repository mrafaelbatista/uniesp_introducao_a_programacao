escolha = int(input("Escolha um feitiço (1: Fogo, 2: Água, 3: Terra): "))

match escolha:
    case 1:
        print("Você escolheu o feitiço de Fogo!")
    case 2:
        print("Você escolheu o feitiço de Água!")
    case 3:
        print("Você escolheu o feitiço de Terra!")
    case _:
        print("Escolha inválida.")
