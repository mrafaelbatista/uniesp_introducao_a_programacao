dicionario = {
    1: {
        'nome': 'João',
        'email': 'm@m.com.br',
        'telefone': 99999999,
        'qualificacao': ['Direito', 'C. Contabeis']
    },
    2: {
        'nome': 'Pedro',
        'email': 'p@p.com.br',
        'telefone': 99991111,
        'qualificacao': {
            'graduacao': "Sistema para Internet",
            'pos': "Segurança da Informação"
        }
    },
}

print(dicionario[1])
print(dicionario[1]['nome'])
print(dicionario[1]['qualificacao'][0])
print(dicionario[2]['qualificacao']['pos'])