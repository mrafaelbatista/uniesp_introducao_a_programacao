import requests
import json

def chamarAPI(nome, lat, log):
    
    API_KEY = '2f2f555888d23e5a36c5aad583ebfae9'
    url = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={log}&appid={API_KEY}")

    resposta   = requests.request("GET", url)
    objetos    = json.loads(resposta.text)
    # dados      = objetos['dados']

    # print(objetos)
    print(objetos['name'])
    with open(f"{nome}.json", 'w', encoding='utf-8') as arquivo:
        json.dump(objetos, arquivo)




with open("exemplos\locais.txt", "r", encoding="utf-8") as arquivo:
   # Criando uma "repetição" para ler por linhas
    for linha in arquivo:
        # Imprimindo a linha lida
        lista = linha.rstrip().split(";")
        chamarAPI(nome=lista[0], lat=lista[1], log=lista[2])
