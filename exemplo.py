import requests
import json

API_KEY = '2f2f555888d23e5a36c5aad583ebfae9'
LAT = 50.45466
LOG = 30.5238
url = (f"https://api.openweathermap.org/data/2.5/weather
?lat={LAT}&lon={LOG}&appid={API_KEY}")

resposta   = requests.request("GET", url)
objetos    = json.loads(resposta.text)
# dados      = objetos['dados']

# print(objetos)
print(objetos['name'])
print(type(objetos))

# for i in objetos:
#     print(f"{i} :: {objetos[i]}")

# https://api.openweathermap.org/data/2.5/weather?lat={-7.11532}&lon={-34.861}&appid={2f2f555888d23e5a36c5aad583ebfae9}