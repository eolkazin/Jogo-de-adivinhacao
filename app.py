import random
import os

erro = 0
sorteio = random.randrange(1, 10)

jogador = int(input("numero:"))

while (sorteio != jogador):
    if sorteio > jogador:
        os.system('cls')
        print("O número é maior")
    else:
        print("O número é menor")
    
    erro += 1
    jogador = int(input("numero:"))

print("Você acertou o número!")
print("Você errou", erro, "vezes")
