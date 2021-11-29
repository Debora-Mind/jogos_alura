def jogar():

    abertura()

    palavra_secreta = "banana"
    palavras = ["_" for letras in palavra_secreta]
    print(palavras)

    enforcado = False
    acertou = False
    erros = 0

    while (not enforcado or not acertou):
        chute = input("Digite uma letra")

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (letra == chute):
                    palavras[index] = letra
                index += 1
        else:
            erros += 1
        print (palavras)

    print("Fim de jogo.")

def abertura():
    print("**********************************")
    print("***Bem vindo ao jogo da forca!****")
    print("**********************************")

if (__name__ == "__main__"):
    jogar()