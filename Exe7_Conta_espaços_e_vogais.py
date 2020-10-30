def String(frase):
    print(f"A frase digitada foi: {frase}")
    print(f"Contem" , frase.count(" "), "espaços em branco")
    print("A vogal a apareceu ",frase.count("a"), "vezes")
    print("A vogal e apareceu ",frase.count("e"), "vezes")
    print("A vogal i apareceu ",frase.count("i"), "vezes")
    print("A vogal o apareceu ",frase.count("o"), "vezes")
    print("A vogal u apareceu ",frase.count("u"), "vezes")



frase = str(input("Digite uma frase qualquer: "))
String(frase)


