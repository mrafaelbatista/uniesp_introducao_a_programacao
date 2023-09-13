# Problema da atualização de senha
import time
from datetime import datetime

dias = 5
while dias > 0:
    print(f'{datetime.now()} | Atualize sua senha!'
          f' Faltam {dias} dias.')
    # dias = dias - 1
    dias -= 1
    time.sleep(5)

print('\n---- Estruturas de Repetição ----\n')

for i in range(5, 0, -1):
    print(f'{datetime.now()} | Atualize sua senha!'
          f' Faltam {i} dias.')
    time.sleep(5)
