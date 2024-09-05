# Solicita ao usuário que insira o número correspondente ao voto
voto = int(input("Digite o número correspondente ao candidato (1 para A, 2 para B, 3 para C): "))

# Verifica a opção de voto e informa a qual candidato o voto foi destinado ou se foi nulo
if voto == 1:
    print("Seu voto foi para o candidato A.")
elif voto == 2:
    print("Seu voto foi para o candidato B.")
elif voto == 3:
    print("Seu voto foi para o candidato C.")
else:
    print("Seu voto foi nulo.")
