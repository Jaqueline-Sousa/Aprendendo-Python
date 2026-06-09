navio = [
    ["~", "~", "~", "~"],
    ["~", "~", "~", "~"],
    ["~", "~", "n", "~"],
    ["~", "~", "~", "~"]
]



print("  Bem vindo a batalha Naval da Jaqueline! ")

print("O oceano é 4x4. Tente adivinhar as coordenadas (0 a 3).\n")

while True:

    linha = int(input("Digite a linha (0 a 3): "))
    coluna = int(input("Digite a coluna (0 a 3): "))

    if navio[linha][coluna] == "n":
        print("\n💥 Você afundou o navio! Parabéns!")
        break

    print(" Vish, tente de novo, acertou a água!\n")