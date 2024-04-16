import time
for i in range(1, 11):
    for j in range(1, 11):
        with open('tabuada.txt', 'a') as arquivo:
            arquivo.write(f'{i} * {j} = {i*j}\n')
            print(f'{i} * {j} = {i*j}')
            time.sleep(1)


