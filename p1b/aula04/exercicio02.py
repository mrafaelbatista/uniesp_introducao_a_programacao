nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))

media = (nota1 + nota2) / 2

if media >= 6.0 and media <= 10.0:
    print("Aluno aprovado!")
    print(f"Média: {media}")

elif media < 6.0 and media >= 0.0:
    print("Aluno reprovado!")
    print(f"Média: {media}")

else:
    print("Valor incorreto!")