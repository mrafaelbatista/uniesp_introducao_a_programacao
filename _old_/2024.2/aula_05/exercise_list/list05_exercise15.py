energia = int(input("Energia do portal (%): "))
coordenadas_precisas = input("Coordenadas de destino estão precisas? (sim/não): ").lower()
tempo_ajustado = input("O tempo está ajustado corretamente? (sim/não): ").lower()

if energia > 80 and coordenadas_precisas == "sim" and tempo_ajustado == "sim":
    print("O portal pode ser ativado!")
else:
    if energia <= 80:
        print("Energia insuficiente para ativar o portal.")
    if coordenadas_precisas != "sim":
        print("Coordenadas imprecisas.")
    if tempo_ajustado != "sim":
        print("Tempo não ajustado corretamente.")
