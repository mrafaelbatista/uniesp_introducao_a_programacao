for multiplicador in range(0, 11):

    print("Tabuada do {} ----- ".format(multiplicador))

    for multiplicando in range(0, 11):

        resultado = multiplicador * multiplicando
        print(str(multiplicador) + "x" + str(multiplicando) \
            + " = " + str(resultado))