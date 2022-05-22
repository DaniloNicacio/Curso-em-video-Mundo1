distancia = float(input("Digite a distancia da viagem: \n"))

if distancia <= 200:
    print(f"O custo da viagem será de: R${distancia * 0.50}\n")
else:
    print(f"O custo da viagem será de: R${distancia * 0.45}\n")