def nome_em_caixa_alta(nome) -> str:
    nome = nome.upper()
    return nome


def calcular_media(a, b, c):
    media = (a + b + c) / 3
    return media


texto = nome_em_caixa_alta('vascão!')
print(f'O meu texto em caixa alta é {texto}')

print('--- --- --- --- ---')

result_media = calcular_media(3, 5, 7)
print(f'O resultado da média é {result_media}')