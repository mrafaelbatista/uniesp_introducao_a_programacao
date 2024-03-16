import time


class Estabelecimento:

    def _init_(self, nome,):
        self.nome = nome

    def exibir_menu(self):
        pass



# Classe concreta para o tipo de estabelecimento "Restaurante"
class Restaurante(Estabelecimento):
    def exibir_menu(self):
        return f"MENU DO RESTAURANTE: {self.nome} \n lagosta \n camarão\n bifes \n bebidas"


# Classe concreta para o tipo de estabelecimento "Lanchonete"

class Lanchonete(Estabelecimento):
    def exibir_menu(self):
        return f"Menu da Lanchonete: {self.nome} \n x-tudo \n x-bacon \n X- calabresa"


# Classe concreta para o tipo de estabelecimento "Pizzaria"


class Pizzaria(Estabelecimento):
    def exibir_menu(self):
        return f"Menu da Pizzaria {self.nome} \n cala \n bacon \n queijo"



class Bar(Estabelecimento):
    def exibir_menu(self):
        return f"menu do bar: {self.nome} \n Cervejas \n petiscos \n refrigerantes "



# Classe fábrica responsável por criar os objetos de estabelecimento

# Responsável por criar os objetos de estabelecimento.
class FabricaEstabelecimento:

    # Recebe o tipo de estabelecimento e o nome, e retrona a instância correspondente da classe concreta.
    def criar_estabelecimento(self, tipo_estabelecimento, nome):

        if tipo_estabelecimento == "restaurante":

            return Restaurante(nome)


        elif tipo_estabelecimento == "lanchonete" or "Lanchonete":

            return Lanchonete(nome)


        elif tipo_estabelecimento == "pizzaria":

            return Pizzaria(nome)



        elif tipo_estabelecimento == "Bar" or "bar":

            return Bar(nome)

        else:

            raise ValueError("Tipo de estabelecimento inválido.")


# Uso do Factory Method para criar e exibir os menus dos estabelecimentos


fabrica = FabricaEstabelecimento()

estabelecimentoR = fabrica.criar_estabelecimento("restaurante", "Gulliver")

estabelecimento_Lanche = fabrica.criar_estabelecimento("lanchonete","marcão")

estabelecimentoP = fabrica.criar_estabelecimento("pizzaria","dnapoles")

estabelecimentoB = fabrica.criar_estabelecimento("Bar", "bar do ze")


#NESSA PARTE VERIAMOS COMO FUNCIONARIA COM O USUARIO:

print("Olá usuário, digite o tipo de estabelecimento que você deseja consultar o menu:")
time.sleep(2)

print(" a = restaurante \n b = lanchonete \n c = pizzaria\n d = Bar")
menu = input("Digite aqui:").lower()  # Convertendo a entrada do usuário para minúsculas

if menu == "a":
    print(estabelecimentoR.exibir_menu())
elif menu == "b":
    print(estabelecimento_Lanche.exibir_menu())
elif menu == "c":
    print(estabelecimentoP.exibir_menu())
elif menu == "d":
    print(estabelecimentoB.exibir_menu())