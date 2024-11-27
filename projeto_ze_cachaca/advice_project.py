import requests
from time import sleep
from loguru import logger
from deep_translator import GoogleTranslator

URL = 'https://api.adviceslip.com/advice'

n_conselhos = int(input('Digite a quantidade de conselhos: '))

try:
    for i in range(n_conselhos):
        logger.info(f'Ciclo {i+1} de chamada de API iniciado.')
        # Consultar a API de Conselhos
        result = requests.get(URL)

        logger.success('Chamada de API realizada com sucesso.')

        id = result.json()['slip']['id']
        advice = result.json()['slip']['advice']

        traducao = GoogleTranslator('english', 'portuguese').translate(advice)

        with open('conselhos.txt', 'a', encoding='UTF-8') as arquivo:
            arquivo.write(f'{id} - {advice} - {traducao}\n')
        logger.success('Registro no banco de dados (txt) realizado com sucesso.')

        sleep(1)
        logger.info(f'Fim do ciclo {i+1}.')

except Exception as e:
    logger.exception(e)
