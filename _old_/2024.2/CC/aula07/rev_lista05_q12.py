def validar_arma(ataque, durabilidade, nome_arma):
    
    if ataque > 50 and durabilidade > 70:
        print('Arma validada!')
        return nome_arma
    else:
        return 'error'


if __name__ == '__main__':

    controle_opcao = 1000

    while controle_opcao != -1:
        nome_arma = input('Digite o nome da arma: ')
        ataque_arma = int(input('Digite o ataque da arma: '))
        durabilidade_arma = int(input('Digite a durabilidade da arma: '))

        resultado_validacao = validar_arma(ataque_arma,
                                           durabilidade_arma,
                                           nome_arma)
        
        if resultado_validacao != 'error':
            print(f'A sua arma {resultado_validacao}, foi validada!!!')
        else:
            print('Essa arma não funciona!')

        controle_opcao = int(input('Digite: \n0 para continuar e \n-1 para finalizar'))
