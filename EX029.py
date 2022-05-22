velocidade = float(input("Digite a velocidade do carro: \n"))
if velocidade > 80:
    print(f"Seu carro foi multado no valor de {(velocidade - 80) * 7.00}reais ")
else:
    print("Você não será multado!")