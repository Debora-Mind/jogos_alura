print("**********************************")
print("*Bem vindo ao jogo de advinhação!*")
print("**********************************")

chute = 0
numero_secreto = 54

jogadas = 5

print("Você precisa advinhar um número de 1 à 100!")

while (jogadas != 0):
    chute = int(input("Qual o seu chute?"))

    if (chute == numero_secreto):
        print("Você acertou")
        break
    else:
        print("Você errou")
        jogadas -= 1

print("Fim de jogo!")