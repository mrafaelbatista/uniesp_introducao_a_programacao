nome = input("Digite seu Primeiro Nome: ")
signo = input("Qual seu signo: ")

pessoa = {
    'primeiro_nome': nome,
    'segundo_nome': 'Katharine',
    'idade': 19,
    'cidade': 'João Pessoa'
}

pessoa['signo'] = signo

print(f'Primeiro Nome: {pessoa["primeiro_nome"]}')
print(f'Segundo Nome: {pessoa["segundo_nome"]}')
print(pessoa)