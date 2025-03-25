import customtkinter

def button_click_event():
    dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Test")
    print("Number:", dialog.get_input())


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
customtkinter.deactivate_automatic_dpi_awareness()

app = customtkinter.CTk()
app.geometry('600x440')
app.title('Minha primeira janela!')

mensagem = customtkinter.CTkLabel(app, text='Olá, mundo!')
mensagem.pack(padx=10, pady=10)

val1 = customtkinter.StringVar()
valor1 = customtkinter.CTkEntry(
    app,
    placeholder_text='Digite o seu nome.',
    textvariable=val1)
valor1.pack(padx=10, pady=10)

def meu_nome():
    print('Eu sou Groot!')

botao = customtkinter.CTkButton(
    app,
    text='Calcular',
    command=meu_nome)
botao.pack(padx=10, pady=10)

button = customtkinter.CTkButton(app, text="Open Dialog", command=button_click_event)
button.pack(padx=20, pady=20)

app.mainloop()