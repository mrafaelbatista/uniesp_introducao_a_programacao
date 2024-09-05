import time

for i in range(5):
    print(f'Aviso {i + 1} - Altere sua senha')
    time.sleep(5)

aviso = 0
while aviso < 5:
    print(f'Aviso {aviso + 1} - Altere sua senha')
    aviso += 1 # aviso = aviso + 1
    time.sleep(5)


