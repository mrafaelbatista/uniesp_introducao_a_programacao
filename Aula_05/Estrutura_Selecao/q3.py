macas = int(input("Digite um número: "))

if macas >= 12:
    resultado = macas * 1.0
    print("Comprei {} por apenas R$ {}.".format(macas, resultado))

else:
    resultado = macas * 1.3
    print("Comprei {} por apenas R$ {}.".format(macas, resultado))