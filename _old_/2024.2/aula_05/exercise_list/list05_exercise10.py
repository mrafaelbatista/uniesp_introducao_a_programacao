porta = int(input("Escolha uma porta (1 a 5): "))

match porta:
    case 1:
        print("Desafio 1: Enigma do Esfinge!")
    case 2:
        print("Desafio 2: Labirinto das Sombras!")
    case 3:
        print("Desafio 3: Prova de Agilidade!")
    case 4:
        print("Desafio 4: Riacho da Verdade!")
    case 5:
        print("Desafio 5: Portal do Destino!")
    case _:
        print("Porta inválida.")
