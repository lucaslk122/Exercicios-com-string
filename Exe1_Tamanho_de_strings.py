def ComapraStrings(txt1,txt2):
    tamanho_tx1 = len(txt1)
    tamanho_tx2 = len((txt2))
    print(f"Tamanho de  {txt1} : {tamanho_tx1} caracteres")
    print(f"Tamanho de  {txt2} : {tamanho_tx2} caracteres")
    if txt2 != txt1:
        print(f"As duas strings possuem conteúdo diferente.")
    else:
        print("As duas strings possuem o mesmo conteúdo difer.")
    if tamanho_tx1 != tamanho_tx2:
        print("As duas strings são de tamanhos diferentes.")
    else:
        print("As duas strings são do mesmo tamanho")


txt1 = input("Digite alguma coisa em formato de texto: ")
txt2 = input("Digite alguma coisa em formato de texto: ")
ComapraStrings(txt1,txt2)