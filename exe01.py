litrocombustivel= float(input("Quantos litros de combustivel voce colocou? \n"))
combustivel = input("Digite seu combustivel  \n"
                    "G or g para Gasolina\n"
                    "E or e para Etanol\n")

vGas = 6.5
vEta = 4.9

if combustivel == 'G' or 'g':
        valorgasolina = litrocombustivel * vGas
        print(f"Você abasteceu {litrocombustivel} e gastou {valorgasolina} de Gasolina\n")
else:
    if combustivel == 'E' or 'e':
        valoretanol = litrocombustivel * vEta
        print(f"Você abasteceu {litrocombustivel} e gastou {valoretanol} de etanol\n")