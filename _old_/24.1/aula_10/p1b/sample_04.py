from loguru import logger

filename = 'arquivo_qn_existe.txt'

try: 
    with open(filename, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

except FileNotFoundError as e:
    logger.error(f'Error: {e}')