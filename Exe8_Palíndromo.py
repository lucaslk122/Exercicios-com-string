def palindromo(frase):
    if frase.replace(" ","") == frase[::-1].replace(" ",""):
        print("É palindromo")
    else:
        print("Não é palindromo")


frase = input("Digite uma frase: ")
palindromo(frase)

print("O que é um para N, pra voce?")