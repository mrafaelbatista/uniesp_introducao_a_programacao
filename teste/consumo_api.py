import json
import requests
from deep_translator import GoogleTranslator

url = 'https://api.adviceslip.com/advice'

for i in range(10):
    result = requests.request("GET", url)
    lista = json.loads(result.text)
    texto1 = lista["slip"]["advice"]
    print(texto1)

    texto = GoogleTranslator(source='english', target='portuguese').translate(texto1)
    print(texto)