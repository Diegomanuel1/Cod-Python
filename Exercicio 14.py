def validar_cpf(cpf):

    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se tem 11 dígitos ou se todos são iguais
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    # Verifica se os dígitos calculados são iguais aos informados
    if cpf[-2:] == f"{digito1}{digito2}":
        return True
    else:
        return False