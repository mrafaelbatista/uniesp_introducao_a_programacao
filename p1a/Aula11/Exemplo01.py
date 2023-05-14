# Imprimindo todo o conteúdo
with open('arquivo.txt', 'r', encoding='UTF-8') as fs:
    conteudo = fs.read()
    print(conteudo)

# Imprimindo por linha
with open('arquivo.txt', 'r', encoding='UTF-8') as fs:
    conteudo = fs.readlines()

    for linha in conteudo:
        print(linha)