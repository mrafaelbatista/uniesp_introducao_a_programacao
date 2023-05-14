# Escrevendo em um arquivo txt
with open('meu_clube.txt', 'w', encoding='utf-8') as fs:
    fs.write('Vasco da Gama\n')
    fs.write('Vasco está melhorando\n')
    fs.write('Mas, o time ainda não é o ideal.\n')