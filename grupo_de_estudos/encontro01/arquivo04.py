import time
from loguru import logger

# Criando um Menu para meus códigos
print('--- Iniciando o Programa ---')

# Menu
while True:
    print('1 - Cadastrar o nome')
    print('2 - Alterar o nome')
    print('3 - Sair')
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            logger.info('O nome foi cadastrado!')
        case 2:
            logger.info('O nome foi alterado!')
        case 3:
            logger.warning('Saindo do programa')
            break

    logger.info('Finalizando o ciclo do menu')
    time.sleep(1)