km = int(input("Insira a quantidade de km percorridos: \n"))
dias = int(input("Quantos dias ele foi alugado?: \n"))

print(f"O custo do aluguel diário ficou em R$:{dias * 60}\n Custo por km rodado R$:{km * 0.15}\n Custo total R$:{(dias*60)+(km*0.15)}")
