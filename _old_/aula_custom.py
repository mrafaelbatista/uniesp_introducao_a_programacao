import customtkinter

customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')

app = customtkinter.CTk()
app.geometry("400x240")
app.title("Minha primeira janela")

mensagem = customtkinter.CTkLabel(app, text='Olá mundo!')
mensagem.pack(padx=10, pady=10)

val1 = customtkinter.StringVar()
input = customtkinter.CTkEntry(
    app,
    placeholder_text='Digite um texto',
    textvariable=val1)
input.pack(padx=10, pady=10)

val2 = customtkinter.StringVar()
input2 = customtkinter.CTkEntry(
    app,
    placeholder_text='Digite um texto',
    textvariable=val2)
input2.pack(padx=10, pady=10)

result = customtkinter.CTkLabel(
    app,
    text='',
    font=('Arial', 24))
result.pack(padx=10, pady=10)

def somar():
    resultado = int(val1.get()) + int(val2.get())
    print(f'Resultado: {resultado}')
    result.configure(text=f"{resultado}")

botao = customtkinter.CTkButton(app, text='Calcular', command=somar)
botao.pack(padx=10, pady=10)



app.mainloop()