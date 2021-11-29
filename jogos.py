import advinhacao
import forca

def escolher_jogo():
    print("*********************")
    print("*Escolha o seu jogo!*")
    print("*********************")

    escolha = int(input("(1) - Advinhação \n(2) - Forca \n"))

    if (escolha == 1):
        advinhacao.jogar()
    elif (escolha == 2):
        forca.jogar()


if (__name__ == "__main__"):
    escolher_jogo()