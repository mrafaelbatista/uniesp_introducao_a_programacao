# Lista de listas representando uma tabela
tabela = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Busca por um elemento na tabela
elemento_busca = 5
encontrado = False
for linha in tabela:
    if elemento_busca in linha:
        encontrado = True
        break
if encontrado:
    print(f"O elemento {elemento_busca} foi encontrado na tabela.")
else:
    print(f"O elemento {elemento_busca} não foi encontrado na tabela.")
