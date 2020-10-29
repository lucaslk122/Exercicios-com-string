def MesPorExtenso(mes):
    if mes == 1:
        return "Janeiro"
    elif mes == 2:
        return "Fevereiro"
    elif mes == 3:
        return "Março"
    elif mes == 4:
        return "Abril"
    elif mes == 5:
        return "Maio"
    elif mes == 6:
        return "Junho"
    elif mes == 7:
        return "Julho"
    elif mes == 8:
        return "Agosto"
    elif mes == 9:
        return "Setembro"
    elif mes == 10:
        return "Outubro"
    elif mes == 11:
        return "Novembro"
    else:
        return "Dezembro"

print("Data de nascimento, digite no formato DD/mm/AAAA")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
print(f"Data de nascimento: {dia}/{mes}/{ano}")
print(f"Você nasceu em {dia} de {MesPorExtenso(mes)} de {ano}")