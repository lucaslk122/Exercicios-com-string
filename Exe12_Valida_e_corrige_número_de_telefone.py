print("Valida e corrige número de telefone")
telefone = input("Telefone: ")
print(len(telefone))
if len(telefone) == 7:
    print("Telefone possui 7 dígitos. Vou acrescentar o digito três na frente")
    telefone_corrigido = telefone[0] = 3
    print(f"Telefone corrigido: {telefone_corrigido}")
