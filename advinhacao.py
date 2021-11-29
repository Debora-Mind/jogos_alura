print("**********************************")
print("*Bem vindo ao jogo de advinhação!*")
print("**********************************")

chute = 0
numero_secreto = 54

jogadas = 5

print("Você precisa advinhar um número de 1 à 100!")

while (jogadas != 0):
    chute = int(input("Qual o seu chute? "))

    if (chute == numero_secreto):
        print("Você acertou")
        break
    elif (chute > numero_secreto):
        print("Seu chute foi maior que o número secreto!")
        jogadas -= 1
    else:
        print("Seu chute foi menor do que o número secreto!")

    print("Você ainda tem {} chances".format(jogadas))

print("Fim de jogo!")