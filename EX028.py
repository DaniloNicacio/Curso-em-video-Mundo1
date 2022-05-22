from random import randint

while(True):
    n = randint(0, 5)
    n_usuario = int(input("Digite um número entre 0 e 5: \n"))
    if n == n_usuario:
        print("Você venceu!")
    else:
        print("Você perdeu")