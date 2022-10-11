'''A variável nome recebe o retorno da função input.
input() tem um argumento que é a mensagem passada no
terminal, e recebe um valor digitado no teclado.
Seu retorno é fundamentalmente uma String'''
nome = input("Digite seu nome, por favor: ")

'''A função print, abaixo, recebe uma string formatada.
A formatação permite passar uma variável entre chaves,
tornando o texto impresso mais flexível'''
print(f"Bom dia, {nome}!")