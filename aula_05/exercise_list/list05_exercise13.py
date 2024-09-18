posicao_exercito = input("O exército está dentro ou fora do castelo? ").lower()

match posicao_exercito:
    case "dentro":
        print("Sistema de defesa desativado.")
    case "fora":
        print("Sistema de defesa ativado.")
    case _:
        print("Posição inválida.")
