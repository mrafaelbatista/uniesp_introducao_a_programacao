import requests

URL = 'https://api.adviceslip.com/advice'

for i in range(10):
    resposta = requests.get(URL)

    # print(resposta)
    # print(resposta.text)
    # print(resposta.json())
    print(resposta.json()['slip']['advice'])