hora1 = int(input(" Digite um hora ate 12h\n"))
minuto1 =float(input("Digite quantos minutos\n"))

hora2 = int(input(" Digite um hora ate 24h\n"))
minuto2 =float(input("Digite quantos minutos\n"))

somahora = hora1 + hora2
somaminuto = (minuto1 + minuto2)


if somahora > 12:
    somatotal = somatotal - 12
p   rint(f"{somatotal}")
