# Desenvolva um programa que gere os primeiros N números
# da sequência de Fibonacci
if __name__ == '__main__':

    # onde N é fornecido pelo usuário
    n = int(input('Digite o número desejado: '))
    
    fn1 = 0
    fn2 = 1
    
    # Utilize um loop para calcular e exibir os termos da sequência.
    for i in range(n):
        resultado = fn1 + fn2
        fn1 = fn2
        fn2 = resultado

        print(f'Resultado: {resultado} | fn1 => {fn1} | fn2 => {fn2}')
