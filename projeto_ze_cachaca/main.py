from loguru import logger

lista_de_frutas = ['maçã', 'uva']

try:
    print(lista_de_frutas[5])
    print(50/0)

except IndexError as error:
    logger.warning('Sua lista não tem a quantidade de objetos indicada!')
    logger.error(f'Error: {error}')

except ZeroDivisionError as error:
    logger.warning('Você não pode dividir um valor por zero')
    logger.error(f'Error: {error}')

except Exception as error:
    print(f'Error: {error}')


print('Finalizando o programa!!!')