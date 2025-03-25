nota1_candidato1 = float(input("Nota 1 do Candidato 1: "))
nota2_candidato1 = float(input("Nota 2 do Candidato 1: "))
nota3_candidato1 = float(input("Nota 3 do Candidato 1: "))
media_candidato1 = (nota1_candidato1 + nota2_candidato1 + nota3_candidato1) / 3

nota1_candidato2 = float(input("Nota 1 do Candidato 2: "))
nota2_candidato2 = float(input("Nota 2 do Candidato 2: "))
nota3_candidato2 = float(input("Nota 3 do Candidato 2: "))
media_candidato2 = (nota1_candidato2 + nota2_candidato2 + nota3_candidato2) / 3

nota1_candidato3 = float(input("Nota 1 do Candidato 3: "))
nota2_candidato3 = float(input("Nota 2 do Candidato 3: "))
nota3_candidato3 = float(input("Nota 3 do Candidato 3: "))
media_candidato3 = (nota1_candidato3 + nota2_candidato3 + nota3_candidato3) / 3

if media_candidato1 > media_candidato2 and media_candidato1 > media_candidato3:
    print("Candidato 1 é o vencedor!")
elif media_candidato2 > media_candidato1 and media_candidato2 > media_candidato3:
    print("Candidato 2 é o vencedor!")
elif media_candidato3 > media_candidato1 and media_candidato3 > media_candidato2:
    print("Candidato 3 é o vencedor!")
else:
    print("Há um empate!")
