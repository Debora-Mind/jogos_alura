import random


def jogar():

    abertura()
    numero_secreto = gerando_numero_secreto()

    jogadas = escolher_dificuldade()

    print("Você precisa advinhar um número de 1 à 100!")

    venceu = resultado(jogadas, numero_secreto)

    if (venceu == True):
        menssagem_vencedora()
    else:
        menssagem_perdedora(numero_secreto)

    print("Fim de jogo!")


def abertura():
    print("**********************************")
    print("*Bem vindo ao jogo de advinhação!*")
    print("**********************************")


def gerando_numero_secreto():
    return random.randrange(1,101)


def escolher_dificuldade():
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
    return jogadas


def resultado(jogadas, numero_secreto):

    pontos = 1000

    for rodada in range(1, jogadas + 1):
        rodada = jogadas - rodada

        chute = int(input("Qual o seu chute? "))

        if (chute <1 or chute >100):
            print("Você deve digitar um número entre 1 e 100! (Perde 1 rodada!)")
            print("Você ainda tem {} chances de {}\n".format(rodada, jogadas))
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        perdeu = rodada == 0

        if (acertou):
            print("Sua pontuação foi {}".format(pontos))
            return True
        elif (maior):
            print("Seu chute foi maior que o número secreto!")
            pontos = pontos - abs(chute - numero_secreto)
        elif (menor):
            print("Seu chute foi menor do que o número secreto!")
            pontos = pontos - abs(chute - numero_secreto)

        if (not perdeu):
            print("Você ainda tem {} chances de {}\n".format(rodada, jogadas))
        elif (perdeu):
            print("Sua pontuação foi {}".format(pontos))
            return False


def menssagem_vencedora():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def menssagem_perdedora(numero_secreto):
    print("Puxa, você perdeu!")
    print("O número secreto era {}".format(numero_secreto))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if (__name__ == "__main__"):
    jogar()