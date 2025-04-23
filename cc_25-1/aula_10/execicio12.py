# Entrada de Dados
la = int(input('Digite o Lado A: '))
lb = int(input('Digite o Lado B: '))
lc = int(input('Digite o Lado C: '))

# Processamento e Saída
if la == lb == lc:
    print('Equilátero!')
elif la == lb or lb == lc or lc == la:
    print('Isóceles!')
elif la != lb != lc:
    print('Escaleno!')

