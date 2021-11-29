import random

def jogar():

    abertura()
    palavra_secreta = gerando_palavra_secreta()

    palavra_descoberta = gerando_palavra_descoberta(palavra_secreta)
    print(palavra_descoberta)

    enforcado = False
    acertou = False
    erros = 0

    while (not enforcado or not acertou):
        chute = input("Digite uma letra")

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (letra == chute):
                    palavra_descoberta[index] = letra
                index += 1
                if (letra != chute):
                    erros += 1

        enforcado = erros == 7
        acertou = not "_" in palavra_descoberta

        if (acertou):
            menssagem_vencedora()
            break
        elif (enforcado):
            menssagem_perdedora()

        print (palavra_descoberta)

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

def menssagem_vencedora():
    pass

def menssagem_perdedora():
    pass
if (__name__ == "__main__"):
    jogar()