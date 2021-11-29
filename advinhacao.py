import random

print("**********************************")
print("*Bem vindo ao jogo de advinhação!*")
print("**********************************")

chute = 0
numero_secreto = random.randrange(1,101)

jogadas = 0
dificuldade = 0
pontos = 1000

print("Você precisa advinhar um número de 1 à 100!")

print("Escolha a dificuldade:")
dificuldade = int(input("(1) - Fácil  (2) - Médio  (3) - Difícil "))
if dificuldade == 1:
    print("Facíl foi selecionado!\n")
    jogadas = 20
elif dificuldade == 2:
    print("Médio foi selecionado!\n")
    jogadas = 10
else:
    print("Difícil foi selecionado!\n")
    jogadas = 5

for rodada in range(1, jogadas + 1):
    rodada = jogadas - rodada

    chute = int(input("Qual o seu chute? "))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    perdeu = rodada == 0

    if (acertou):
        print("Você acertou")
        print("Sua pontuação foi {}".format(pontos))
        break
    elif (maior):
        print("Seu chute foi maior que o número secreto!")
        pontos = pontos - abs(chute - numero_secreto)
    elif (menor):
        print("Seu chute foi menor do que o número secreto!")
        pontos = pontos - abs(chute - numero_secreto)

    if (not perdeu):
        print("Você ainda tem {} chances de {}\n".format(rodada, jogadas))
    elif (perdeu):
        print("Você perdeu!")
        print("Sua pontuação foi {}".format(pontos))
        print("O número secreto era {}".format(numero_secreto))

print("Fim de jogo!")