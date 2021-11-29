print("**********************************")
print("*Bem vindo ao jogo de advinhação!*")
print("**********************************")

chute = 0
numero_secreto = 54

jogadas = 0
dificuldade = 0

print("Você precisa advinhar um número de 1 à 100!")

print("Escolha a dificuldade:")
dificuldade = int(input("(1) - Fácil  (2) - Médio  (3) - Difícil "))
if dificuldade == 1:
    jogadas = 20
elif dificuldade == 2:
    jogadas = 10
else:
    jogadas = 5

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
        jogadas -= 1

    if (jogadas != 0):
        print("Você ainda tem {} chances".format(jogadas))
    elif (jogadas == 0):
        print("Você perdeu!")
        print("O número secreto era {}".format(numero_secreto))

print("Fim de jogo!")