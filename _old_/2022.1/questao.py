controle = 100

while controle > 0:

    if (controle % 2) == 0:
        print(f"O valor {controle} é par!")
        if (controle % 5) == 0:
            print(f"O valor {controle} é multiplo de 5!")
    else:
        print("----")

    controle -= 1