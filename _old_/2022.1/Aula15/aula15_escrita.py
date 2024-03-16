with open("aula15.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

nome = "Messias"
with open("arquivo_da_aula.txt", "a", encoding="utf-8") as arquivo:
    for line in range(10):
        arquivo.write(f"{line} - Meu nome é {nome}\n")