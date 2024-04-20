import time

spam = 0
control = True

while control:
    print(f'Este é meu spam n {spam}')
    # time.sleep(2)
    # spam = spam + 1
    spam += 1
    if spam == 1000000:
        control = False
