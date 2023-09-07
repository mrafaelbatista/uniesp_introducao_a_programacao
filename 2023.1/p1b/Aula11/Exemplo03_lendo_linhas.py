with open('meu_arquivo.txt', 'r', encoding='utf-8') as fs:
    linhas = fs.readlines()

print(f'Linhas é do tipo {linhas}')
print('\n')

for linha in linhas:
    print(linha.rstrip())

