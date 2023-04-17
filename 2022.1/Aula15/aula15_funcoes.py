# def nome_soma(numero1, numero2):
#     nome = input("Digite seu nome: ")
#     print(nome)
#     print(numero1 + numero2)

# nome_soma(numero1=10, numero2=15)

# def imprimitr_num(inicial, final):
    
#     for i in range(inicial, final):
#         print(i)

# imprimitr_num(10, 20)

# def bom_dia(nome):
#     print("Tenha um bom dia...")

# bom_dia()
# bom_dia()

def ler_arquivo(nome_arquivo):

    with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("Funcionou")

ler_arquivo("aula15.txt")
ler_arquivo("arquivo_da_aula.txt")



