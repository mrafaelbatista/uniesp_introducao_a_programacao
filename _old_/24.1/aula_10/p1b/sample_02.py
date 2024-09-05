filename = 'arquivo.txt'

# with open(filename, 'r', encoding='utf-8') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# with open(filename, 'r', encoding='utf-8') as arquivo:
#     for linha in arquivo:
#         print(f'[{len(linha.rstrip())}] - {linha.rstrip()}')

with open(filename, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()


for i in linhas:
    print(i)
