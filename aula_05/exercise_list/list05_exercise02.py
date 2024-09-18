ferro = float(input("Digite a quantidade de ferro (kg): "))
ouro = float(input("Digite a quantidade de ouro (kg): "))

total = ferro + ouro

porcentagem_ferro = (ferro / total) * 100

if porcentagem_ferro >= 70:
    print("A liga metálica está adequada!")
else:
    print("A liga metálica não é adequada, precisa de mais ferro.")
