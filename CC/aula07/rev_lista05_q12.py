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


# # Crie um programa que receba os valores de ataque e durabilidade das três armas
# espada_atq = int(input('Digite o ataque da espada: '))
# espada_dur = int(input('Digite a durabilidade da espada: '))

# arco_atq = int(input('Digite o ataque da arco: '))
# arco_dur = int(input('Digite a durabilidade da arco: '))

# lanca_atq = int(input('Digite o ataque da lanca: '))
# lanca_dur = int(input('Digite a durabilidade da lanca: '))

# # determine qual é a mais adequada. => Atq > 50 and Dur > 70
# if espada_atq > 50 and espada_dur > 70:
#     print('Utilize a espada!')
# elif arco_atq > 50 and arco_dur > 70:
#     print('Utilize o arco!')
# elif lanca_atq > 50 and lanca_dur > 70:
#     print('Utilize a lança!')
# else: # Se nenhuma atender, o programa deve sugerir que o herói busque uma nova arma.
#     print('Escolha outra arma!')


