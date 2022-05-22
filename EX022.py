nome = input("Digite seu nome: \n")

print(f"Nome em maiúsculo: {nome.upper()}\n")
print(f"Nome em minúsculo: {nome.lower()}\n")
n_letras = len(nome.replace(" ",""))
print(f"Quantidade de letras no nome: {n_letras}")
n_letras_1nome = len(nome.split()[0])
print(f"Quantidade de letras no primeiro nome: {n_letras_1nome}")