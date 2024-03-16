from xmlrpc.client import Boolean


# Cast = Transformar um tipo de dado em outro
# TRansformando de Str() para Int()
nota = int(input("Digite uma nota: "))

if (nota >= 0) and (nota < 5):
    print("Reprovado")
elif (nota >= 5) and (nota <= 6):
    print("Recuperação!")
elif (nota >= 7) and (nota <= 10):
    print("Aprovado")
else:
    print("Nota fora do intervalo!")
    