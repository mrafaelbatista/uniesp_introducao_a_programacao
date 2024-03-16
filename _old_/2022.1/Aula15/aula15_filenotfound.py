try:
    with open("inexistente.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except Exception as e:
    print(f"O erro foi: {e}")
    print("Não se preocupe, o programa está funcionando!")

for n in range(3):
    print(n)