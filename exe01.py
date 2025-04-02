litrocombustivel= float(input("Quantos litros de combustivel voce colocou? \n"))
combustivel = input("Digite seu combustivel  \n"
                    "G para Gasolina\n"
                    "E para Etanol\n")

vGas = 6.5
vEta = 4.9

if combustivel == 'G':
        valorgasolina = litrocombustivel * vGas
        print(f"Você abasteceu {litrocombustivel} e gastou {valorgasolina} de Gasolina\n")
else:
    if combustivel == 'E':
        valoretanol = litrocombustivel * vEta
        print(f"Você abasteceu {litrocombustivel} e gastou {valoretanol} de etanol\n")