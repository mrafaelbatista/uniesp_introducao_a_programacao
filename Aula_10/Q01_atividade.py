
clubes = ["Flamengo", "Vasco", "Curitinhas", "São Paulo", "Treze", "Sport Recife", "Belo"]

clube = "Vasco"

for c in clubes:
    if c == clube:
        print("Achei")
    else:
        print("Não achei")

if clube in clubes:
    print("Achou")
