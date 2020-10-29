def NomeVertical(nome):
    lista = ""
    for i in nome:
        lista += i
        print(lista)

nome = str(input("digite seu nome: "))
NomeVertical(nome)