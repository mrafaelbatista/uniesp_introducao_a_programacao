import settings_app
import customtkinter

# Configuração das cores do aplicativo
customtkinter.set_appearance_mode(mode_string='light')
customtkinter.set_default_color_theme(color_string='dark-blue')

# Instaciação do aplicativo
app = customtkinter.CTk()

# Funções para funcionamento
def open_toplevel(app=app):
    '''open_toplevel abre uma nova janela toplevel.'''
    toplevel = customtkinter.CTkToplevel(app)
    toplevel.title("Nova Janela")
    toplevel.geometry("400x300")

    label = customtkinter.CTkLabel(toplevel, text="Esta é uma nova janela toplevel", font=('Arial', 14))
    label.pack(padx=20, pady=20)

    registro = customtkinter.CTkEntry(toplevel, placeholder_text="Informe o dado abaixo")
    registro.pack(padx=20, pady=20)

    button = customtkinter.CTkButton(toplevel, text="Fechar", command=lambda: retorno_toplevel(registro.get()))
    button.pack(pady=20)

def retorno_toplevel(value) -> str:
    return str(value)

# Função que adicionar item a lista
def adicionar_vingador(lista, vingador:str):
        lista.append(vingador)
        print("------- Vingador Adicionado -------")
        return lista


# Função para selecionar a opção do menu
def menu_callback(opcao:int):
    if opcao == 1:
        novo_vingador = open_toplevel()
        print(f'O novo vingador é: {novo_vingador}')
        settings_app.lista_avengers = adicionar_vingador(settings_app.lista_avengers, novo_vingador)
    elif opcao == 2:
        textbox_callback(textbox, settings_app.lista_avengers)

# Função de Textbox que mostra os itens da lista
def textbox_callback(textbox, lista:None):
    if (lista is None) or (len(lista) == 0):
        print('Não fez nada!')
    else:
        for i in range(len(lista)):
            textbox.insert(f'{i+1}.0', f'{i} {lista[i]}\n')




# Configuração do nome e tamanho da janela do aplicativo
app.title("Minha aplicação")
app.geometry("600x400")
app.grid_columnconfigure(0, weight=1)

# Texto do Menu de opções
menu = customtkinter.CTkLabel(app, text=settings_app.menu_texto, fg_color="transparent", justify="left", font=('Arial', 16))
menu.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

# Texto da para escolha da opção
opcao_label = customtkinter.CTkLabel(app, text=settings_app.opcao_texto, fg_color="transparent", justify="left", font=('Arial', 16))
opcao_label.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

# Caixa de Entrada da opção desejada
opcao = customtkinter.CTkEntry(app, placeholder_text="Qual sua opção?", )
opcao.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")

# Botão que executar a chamada da função do Menu
button = customtkinter.CTkButton(app, text="Confirmar", command=lambda: menu_callback(int(opcao.get())))
button.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

# Textbox em que aparece os itens da lista
textbox = customtkinter.CTkTextbox(app)
textbox_callback(textbox=textbox, lista=settings_app.lista_avengers)
textbox.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

app.mainloop()