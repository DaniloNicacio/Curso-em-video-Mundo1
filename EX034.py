salario = float(input("Digite um salario qualquer: "))

if salario > 1250.00:
    print(f"Seu aumento será de R${(salario) + (salario*0.10)}")
if salario < 1250.00:
    print(f"Seu aumento será de R${(salario) + (salario*0.15)}")