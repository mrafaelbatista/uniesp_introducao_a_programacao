# Lista de clubes
clubes = ['al hilal', 'vasco', 'barcelona', 'city', 'boca', 'ibis']

# Visualização dos clubes selecionados
print('Clubes escolhidos:')
print(clubes)

# Clube que será pesquisado
pesquisado = 'flamengo'

status_da_busca = False

# Verificação se o clube pesquisado está na lista
for posicao in range(0, len(clubes), 1):
   
   if pesquisado == clubes[posicao]:
      status_da_busca = True

if status_da_busca:
   print('Achei')
else:
   print('Não achei')

print('--- Programa finalizado ---')






