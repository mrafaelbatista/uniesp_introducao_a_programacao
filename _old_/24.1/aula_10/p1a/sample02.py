# with open(file='arquivo.txt', mode='r', encoding='UTF-8') as file:
#     conteudo = file.read()
#     print(conteudo)

# with open(file='arquivo.txt', mode='r', encoding='UTF-8') as file:
#     for linha in file:
#         print(f'{len(linha.rstrip())} - {linha.rstrip()}')

# with open(file='arquivo.txt', mode='r', encoding='UTF-8') as file:
#     linhas = file.readlines()

with open(file='arquivo2.txt', mode='a', encoding='UTF-8') as file:
    file.write('Eu amo SQL!\n')
    file.write('Eu amo Pandas!\n')
    file.write('Eu amo Sklearn!\n')