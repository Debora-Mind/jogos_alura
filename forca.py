import random

def jogar():

    abertura()
    palavra_secreta = gerando_palavra_secreta()

    palavra_descoberta = gerando_palavra_descoberta(palavra_secreta)
    print(palavra_descoberta)

    venceu = resultado(palavra_secreta, palavra_descoberta)

    print("Fim de jogo.")

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
    erros = 7

    while (True):
        chute = input("Digite uma letra: ")

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (letra == chute):
                    palavra_descoberta[index] = letra
                index += 1
        else:
                    erros -= 1
                    print("Você errou! Tem mais {} chances.".format(erros))

        enforcado = erros <= 0
        acertou = not "_" in palavra_descoberta

        if (acertou):
            menssagem_vencedora()
            return True
        elif (enforcado):
            menssagem_perdedora()
            return False

        print (palavra_descoberta)


def menssagem_vencedora():
    print("")



def menssagem_perdedora():
    print("")


if (__name__ == "__main__"):
    jogar()