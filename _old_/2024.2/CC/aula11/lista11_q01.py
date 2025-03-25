lista_de_clubes = []

for i in range(5):
    
    c = input('Digite um novo clube: ')

    # Adicionar o clube a lista
    lista_de_clubes.append(c)

clube_pesquisado = input('Digite seu clube do coração S2: ')

encontrou = False

for clube in lista_de_clubes:
    
    if clube.upper() == clube_pesquisado.upper():
        encontrou = True


for i in range(len(lista_de_clubes)):
    
    if lista_de_clubes[i].upper() == clube_pesquisado.upper():
        encontrou = True 


if encontrou:
    print('Achei!')
else:
    print('Não achei!')



