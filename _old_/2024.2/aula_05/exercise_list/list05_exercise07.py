altura = float(input("Digite a altura da planta (metros): "))

if altura < 1:
    print("A planta é pequena.")
elif 1 <= altura <= 3:
    print("A planta é média.")
else:
    print("A planta é grande.")
