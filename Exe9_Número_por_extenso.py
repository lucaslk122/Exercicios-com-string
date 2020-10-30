def NumeroPorExenso(numero):
    contagem = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove'], \
                 ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    if numero <= 20:
        print(f"Numero por extenso: {contagem[0][numero -1]}")
    else:
        numero = str(numero)
        if numero[1] == '0':
            numero = int(numero[0])
            print(contagem[1][numero -2])
        else:
            numero_d = int(numero[0])
            print(contagem[1][numero_d - 2], end=" e ")
            numero_u = int(numero[1])
            print(contagem[0][numero_u - 1])


while True:
    numero = int(input("Digite um numero entre 0 e 99: "))
    if numero > 0 and numero < 99:
        NumeroPorExenso(numero)
        break
    else:
        print("Numero invalido,digite novamente")