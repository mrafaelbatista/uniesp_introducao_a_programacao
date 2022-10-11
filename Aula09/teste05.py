#por quê o exercicio não funcionou com match/case ????

lista1=[]
lista2=[]
lista3=[]
lista4=[]

numeros=0

while numeros >= 0:

    numeros = int(input('Digite numeros aleatorios (positivos e negativos):'))
        
    match numeros:
            
            case numeros >= 0 and numeros <=25:
                    lista1.append(numeros)
            
            case numeros >=26 and numeros <=50:
                    lista2.append(numeros)
            
            case numeros >=51 and numeros <=75:
                    lista3.append(numeros)
            
            case (numeros >=76 and numeros <=100):
                    lista4.append(numeros)

            case numeros < 0:
                    print('a quantidade de numeros entre:')
                    print(f'0-25 = {len(lista1)}')
                    print(f'26-50 = {len(lista2)}')
                    print(f'51-75 = {len(lista3)}')
                    print(f'76-100 = {len(lista4)}')