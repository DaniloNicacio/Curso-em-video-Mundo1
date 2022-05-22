n = input("Digite um numero de 0 a 9999: \n")
n_dividido = []
for i in n:
    n_dividido.append(i)

print(f"Unidade: {n_dividido[3]}\n Dezena: {n_dividido[2]}\n Centena: {n_dividido[1]}\n Milhar: {n_dividido[0]}\n")