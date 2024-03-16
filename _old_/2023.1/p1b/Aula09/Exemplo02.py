matriz5x5 = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]

for lista in matriz5x5:
    for item in lista:
        if (item % 2) == 0:
            print(f'Este número é PAR {item}')
        elif item == 5:
            print(f'Este é o número cinco - {item}')
        elif (item % 2) != 0:
            print(f'Este número não é cinco e é ímpar {item}')
