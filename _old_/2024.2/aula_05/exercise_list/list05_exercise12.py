ataque_espada = int(input("Poder de ataque da Espada: "))
durabilidade_espada = int(input("Durabilidade da Espada: "))

ataque_arco = int(input("Poder de ataque do Arco: "))
durabilidade_arco = int(input("Durabilidade do Arco: "))

ataque_lanca = int(input("Poder de ataque da Lança: "))
durabilidade_lanca = int(input("Durabilidade da Lança: "))

if ataque_espada > 50 and durabilidade_espada > 70:
    print("A Espada é a melhor escolha.")
elif ataque_arco > 50 and durabilidade_arco > 70:
    print("O Arco é a melhor escolha.")
elif ataque_lanca > 50 and durabilidade_lanca > 70:
    print("A Lança é a melhor escolha.")
else:
    print("Nenhuma das armas é adequada, busque uma nova arma.")
