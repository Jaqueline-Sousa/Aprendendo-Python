import random

palpite = 0
numeroSecreto = random.randint(1, 20)

while palpite != numeroSecreto:
    palpite = int(input("digite um numero entre 1 e 20 tente adivinhar qual está certa: "))
    if palpite < numeroSecreto:
        print("o número secreto é maior")
    elif palpite > numeroSecreto:
        print("o número secreto é menor")

print("Parabéns! Você acertou o número secreto!")