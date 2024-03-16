nome_arquivo = 'vasco.txt'

with open(nome_arquivo, 'w', encoding='UTF-8') as file:
    file.write('Vamos todos cantar de coração!\n')
    file.write('Precisar trocar o técnico!\n')
    print('Processamento finalizado...')

with open(nome_arquivo, 'a', encoding='utf-8') as file:
    file.write('Esse time é muito ruim!!!\n')

with open(nome_arquivo, 'r', encoding='utf-8') as file:
    conteudo = file.read()
    print(conteudo)