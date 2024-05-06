import customtkinter

def open_toplevel(app):
    '''open_toplevel abre uma nova janela toplevel.'''
    toplevel = customtkinter.CTkToplevel(app)
    toplevel.title("Nova Janela")
    toplevel.geometry("400x300")

    label = customtkinter.CTkLabel(toplevel, text="Esta é uma nova janela toplevel", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    button = customtkinter.CTkButton(toplevel, text="Fechar", command=toplevel.destroy)
    button.pack(pady=20)

# Função que adicionar item a lista
def adicionar_vingador(lista:None, vingador:str):
    if lista is None:
        print('Não fez nada!')
    else:
        lista.append(vingador)
        print("------- Vingador Adicionado -------")


# Função para selecionar a opção do menu
def menu_callback(opcao:int, app):
    if opcao == 1:
        open_toplevel(app)
    elif opcao == 2:

# Função de Textbox que mostra os itens da lista
def textbox_callback(textbox, lista:None):
    if (lista is None) or (len(lista) == 0):
        print('Não fez nada!')
    else:
        for i in range(len(lista)):
            textbox.insert(f'{i+1}.0', f'{i} {lista[i]}\n')

