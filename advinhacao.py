print("**********************************")
print("*Bem vindo ao jogo de advinhação!*")
print("**********************************")

chute = 0
numero_secreto = 54

print("Você precisa advinhar um número de 1 à 100!")
chute = input("Qual o seu chute?")

if (chute == numero_secreto):
    print("Você acertou")
else:
    print("Você errou")