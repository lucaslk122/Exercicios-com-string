def MostrarNome(nome):
    inverso = str(nome[::-1]).upper()
    print(f"O nome informado foi {nome} e ele de tras para frente fica {inverso}")


nome = input("digite seu nome: ").lower()
MostrarNome(nome)