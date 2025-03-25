agua_disponivel = float(input("Quantidade de água disponível (litros): "))

distancia = float(input("Distância até o oásis (km): "))

agua_necessaria = distancia * 2

if agua_disponivel >= agua_necessaria:
    print("A quantidade de água é suficiente para chegar ao oásis.")
    
else:
    print("A quantidade de água não é suficiente, será necessário mais água.")
