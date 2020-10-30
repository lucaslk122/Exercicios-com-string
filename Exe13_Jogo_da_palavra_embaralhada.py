palavras_sortear = []
print("Digite PARAR para parar de digitar as palavras")
while True:
    palavras = str(input("Digite uma palavra: "))
    if palavras != "parar" or palavras != "PARAR":
        palavras_sortear.append(palavras)
    else:
        break
print(palavras_sortear)