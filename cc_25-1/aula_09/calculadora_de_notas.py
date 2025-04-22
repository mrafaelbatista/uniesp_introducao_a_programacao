# Lista de notas
notas = []

while True:
    print('Adicione a nota ou digite -1 para sair!')

    valor = int(input('Digite a nota ou -1: '))

    if valor == -1:
        break
    elif 0 <= valor <= 10:
        notas.append(valor)
    else:
        print(f'O valor {valor} é inválido!')

somatorio = 0

for i in range(len(notas)):
    somatorio = somatorio + notas[i]

media = somatorio / len(notas)

print(f'A média final é: {media}')
print(f'As notas são: {notas}')