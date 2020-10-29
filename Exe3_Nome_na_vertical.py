def NomeVertical(nome):
    lista =  [char for char in nome] 
    for i in lista:
        print(i)


nome = input("digite seu nome: ")
NomeVertical(nome)