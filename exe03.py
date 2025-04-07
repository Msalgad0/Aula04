#Desagio 01
hora1 = int(input(" Digite um hora ate 12h\n"))
minuto1 =int(input("Digite quantos minutos\n"))

hora2 = int(input(" Digite um hora ate 24h\n"))
minuto2 =int(input("Digite quantos minutos\n"))

somahora = hora1 + hora2
somaminuto = (minuto1 + minuto2)

if somahora > 12:
    somahora = somahora -12
if somahora> 24:
    somahora = somahora - 24
if somaminuto >= 60:
    somaminuto = somaminuto - 60
    somahora = somahora + 1
print(f"{somahora}:{somaminuto}")

