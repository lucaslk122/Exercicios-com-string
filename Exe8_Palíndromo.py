
def palindromo(frase):
    if frase.replace(" ","") == frase[::-1].replace(" ",""):
        print("É palindromo")
    else:
        print("Não é palindromo")


frase = input("Digite uma frase: ")
palindromo(frase)


"""
print(frase.replace(" ", ""))
print(frase[::-1].replace(" ",""))
"""