convidados = [
    "Coringa", "Thor", "Jesus", "Naruto", "Loki"
]

# Convite
for nome in convidados:
    mensagem = f"Bora pra balada, {nome.upper()}!"
    print(mensagem)

# Quem não poderá ir
print("Jesus: Infelizmente não \
    posso estar no mesmo ambiente que o Loki!")

print("Coringa: Infelizmente não \
    posso estar no mesmo ambiente que o Naruto!")

# Modifique sua lista, substitua os
# desistentes por novos convidados.
convidados[2] = "Madre Tereza"
convidados[0] = "Pinguim"

# Convite
for nome in convidados:
    mensagem = f"Bora pra balada, {nome.upper()}!"
    print(mensagem)