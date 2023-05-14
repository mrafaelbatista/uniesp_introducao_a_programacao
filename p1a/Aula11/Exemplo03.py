# Adicionando ao meu arquivo txt (meu_arquivo.txt)
with open('meu_clube.txt', 'a', encoding='utf-8') as fs:
    fs.write('Mais um linha no meu arquivo.\n')
    fs.write('Mostrando como adicionar texto.\n')