matriz = [
    [1, 2, 3, 4, 5], # 0
    [4, 5, 6], # 1
    [7, 8, 9]] # 2

for lista in matriz:
    print(f"Novo ciclo de lista - {lista}")
    media = 0
    acumuladora = 0
    for item in lista:
        print(f'Item -> {item}')
        acumuladora += item
    media = acumuladora / len(lista)
    print(media)


