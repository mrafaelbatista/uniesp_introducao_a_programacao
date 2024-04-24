import customtkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

app = customtkinter.CTk()
app.geometry("400x240")
app.title("Minha primeira janela")

mensagem = customtkinter.CTkLabel(app, text='Olá mundo!')
mensagem.pack(padx=10, pady=10)

app.mainloop()