# Variáveis
nome = 'Messi'
nome1 = 'João'
nome_completo = 'João Pessoa' # snake case
nomeCompleto = 'Léo Jardim' # camel case

# Tipos de Dados
'Esse é um texto' # String - Permitido no Python
"Esse também é um texto" # String
12 # Inteiro
3.49 # Float
True or False # Boolean

# Constante
URL_BANCO_DE_DADOS = '192.168.13.100:3306'

# Desvios Condicionais
x = 0

if x < 5:
    print('X é menor que 5')
elif x > 5:
    print('X é maior que 5')
else:
    print('X é igual a 5')

# Match-Case
mes = 7

match mes:
    case 1:
        print('Janeiro')
    case 2:
        print('Fevereiro')
    case 3:
        print('Março')
    case 4:
        print('Abril')
    case 5:
        print('Maio')
    case 6:
        print('Junho')
    case 7:
        print('Julho')

# Estruturas de Repetição

# Quando não tenho a quantidade de ciclos
# Contador
while x < 100:
    print(f'O valor de x é {x}')
    x = x + 1

# Quando tenho a quantidade de ciclos definida
for i in range(5):
    print(i)