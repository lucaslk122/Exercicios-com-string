import  random
def JogoPalavras(palavras_sortear):
    palavra_escolhida = random.choice(palavras_sortear)
    tentativas = 6
    desorganizada = "".join(random.sample(palavra_escolhida,len(palavra_escolhida)))
    while True:
        tentativa = input(f"Que palavra é essa? {desorganizada}: ")
        if tentativa != palavra_escolhida:
            print("Voce errou, tente novamente")
            tentativas = tentativas - 1
            if tentativas == 0:
                print("Voce perdeu, suas tentativas zeraram :( ")
                break
        else:
            print("Voce acertou!")
            break

palavras_sortear = []
print("Digite PARAR para parar de digitar as palavras")
while True:
    palavras = str(input("Digite uma palavra: "))
    if palavras.lower() == "parar":
        break
    else:
        palavras_sortear.append(palavras)
print("Voce tem 6 tentativas para acertar qual é a palavra que estara embaralhada!")
JogoPalavras(palavras_sortear)