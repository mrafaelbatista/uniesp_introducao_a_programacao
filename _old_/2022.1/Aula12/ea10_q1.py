clubes = []

for i in range(10):

    clube = input("Digite o novo clube: ")
    clubes.append(clube)

clube_pesquisar = input("Digite o novo clube: ")

# Forma 1 - Simplificado
for c in clubes:
    
    if clube_pesquisar.upper() == str(c).upper():
        print("Achei!")
    else:
        print("Não achei")

# Forma 2
if clube_pesquisar in clubes:
    print("Achei")
else:
    print("Não achei!")



