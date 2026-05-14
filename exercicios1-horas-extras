def calcular_horas():
    nome = input("Digite seu nome: ")
    try:
        horas = float(input("Digite a quantidade de horas trabalhadas: "))
    except ValueError:
        return "Digite um valor válido!"

    jornada = 40

    if horas < 0:
        return "Digite um valor válido!"
    elif horas < jornada:
        horas_faltantes = jornada - horas
        return f"{nome}, você ainda precisa trabalhar {horas_faltantes} horas"
    elif horas > jornada:
        horas_extras = horas - jornada
        return f"{nome}, você trabalhou {horas_extras} horas extras"
    else:
        return f"{nome}, sua jornada está completa!"

print(calcular_horas())
