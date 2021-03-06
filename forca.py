import random

def jogar():

    abertura()
    palavra_secreta = gerando_palavra_secreta()

    palavra_descoberta = gerando_palavra_descoberta(palavra_secreta)
    print(palavra_descoberta)

    venceu = resultado(palavra_secreta, palavra_descoberta)

    if (venceu):
        menssagem_vencedora()
    else:
        menssagem_perdedora(palavra_secreta)

    print("\nFim de jogo.")

def abertura():
    print("**********************************")
    print("***Bem vindo ao jogo da forca!****")
    print("**********************************")

def gerando_palavra_secreta():
    lista = []
    arquivo = open("palavras.txt", "r")

    for i in arquivo:
        palavra = arquivo.readline().strip()
        lista.append(palavra)

    arquivo.close()

    palavra_secreta = lista[random.randrange(0, len(lista))]

    return palavra_secreta

def gerando_palavra_descoberta(palavra_secreta):
    palavra = ["_" for letras in palavra_secreta]
    return palavra


def resultado(palavra_secreta, palavra_descoberta):
    erros = 0

    while (True):
        chute = input("Digite uma letra: ")

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (letra == chute):
                    palavra_descoberta[index] = letra
                index += 1
        else:
            erros += 1
            desenhar_forca(erros)

        enforcado = erros == 7
        acertou = not "_" in palavra_descoberta

        if (acertou):
            return True
        elif (enforcado):
            return False

        print ("\n", palavra_descoberta)


def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def menssagem_vencedora():
    print("Parab??ns, voc?? ganhou!")
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



def menssagem_perdedora(palavra_secreta):
    print("Puxa, voc?? foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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