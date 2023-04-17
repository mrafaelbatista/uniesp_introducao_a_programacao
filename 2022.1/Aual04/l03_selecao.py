macas = int(input("Quantas maçãs você deseja? "))

if macas >= 12:
    valor = macas * 1
    print(f"Você pediu {macas} maçãs, e custou R$ {float(valor)}")
else:
    valor = macas * 1.3
    print(f"Você pediu {macas} maçãs, e custou R$ {float(valor)}")
