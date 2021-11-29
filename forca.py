print("**********************************")
print("***Bem vindo ao jogo da forca!****")
print("**********************************")

palavra_secreta = "banana"
tentativas = 10
chute = ""

for rodada in range(tentativas):
    chute = input("Digite uma letra: ")

    if (chute in palavra_secreta):
        print(chute)
    else:
        print("Errou...")

print("Fim de jogo.")