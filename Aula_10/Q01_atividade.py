
clubes = ["Flamengo", "Vasco", "Corintinhas", "São Paulo", "Treze", "Sport Recife", "Belo"]

clube = "Vasco"

# Solução 01
for c in clubes:
    if c == clube:
        print("Achei")
    else:
        print("Não achei")

# Solução 02
if clube in clubes:
    print("Achou")
else:
    print("Não achei")
