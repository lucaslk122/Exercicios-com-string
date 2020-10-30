def ValidaCPF(cpf):
    if cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":
        return "Cpf invalido"
    else:
        return "CPF válido"

cpf = input("Digite o cpf no formato xxx.xxx.xxx-xx: ")
print(ValidaCPF(cpf))