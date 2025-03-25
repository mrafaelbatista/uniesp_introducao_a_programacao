# Seção 1 - Importações de bibliotecas, classes e funções
import datetime

# Seção 2 - Definição de funções
def get_data():
    return datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# Seção 3 - Execução do programa
if __name__ == '__main__':

    print(get_data())
    print('Fim do programa')
