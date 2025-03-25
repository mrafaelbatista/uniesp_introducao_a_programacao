ataque_guerreiro1 = int(input("Ataque do Guerreiro 1: "))
defesa_guerreiro1 = int(input("Defesa do Guerreiro 1: "))

ataque_guerreiro2 = int(input("Ataque do Guerreiro 2: "))
defesa_guerreiro2 = int(input("Defesa do Guerreiro 2: "))

poder_guerreiro1 = ataque_guerreiro1 + defesa_guerreiro1
poder_guerreiro2 = ataque_guerreiro2 + defesa_guerreiro2

if poder_guerreiro1 > poder_guerreiro2:
    print("Guerreiro 1 é o vencedor!")
elif poder_guerreiro2 > poder_guerreiro1:
    print("Guerreiro 2 é o vencedor!")
else:
    if defesa_guerreiro1 > defesa_guerreiro2:
        print("Guerreiro 1 é o vencedor pelo critério de defesa!")
    elif defesa_guerreiro2 > defesa_guerreiro1:
        print("Guerreiro 2 é o vencedor pelo critério de defesa!")
    else:
        print("O duelo terminou em empate!")
