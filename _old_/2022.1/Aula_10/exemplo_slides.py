frutas = ["Pêra", "Uva", "Maçã", "Kiwi"]

print(frutas)

frutas[1] = "Carambola"
frutas[2] = "Pitaya"

print(frutas)

indice_fruta = frutas.index("Kiwi")

print(indice_fruta)

del frutas[indice_fruta]

print(frutas)

frutas.remove("Carambola")

print(frutas)

frutas.append("Abacaxi")
frutas.append("Banana")
frutas.append("Uva")
frutas.append("Melão")
frutas.append("Pitanga")

frutas.insert(3, "Pitomba")

print(frutas)

i = frutas.index("Uva")
fruta_pop = frutas.pop(i)
print(frutas)
print(fruta_pop)
