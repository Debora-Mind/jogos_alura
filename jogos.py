import advinhacao

def escolher_jogo():
    print("*********************")
    print("*Escolha o seu jogo!*")
    print("*********************")

    escolha = int(input("(1) - Advinhação\n"))

    if (escolha == 1):
        advinhacao.jogar()

if (__name__ == "__main__"):
    escolher_jogo()