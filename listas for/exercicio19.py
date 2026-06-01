soma_total = 0

print("Digite os números que deseja somar. Para encerrar e ver o total, digite 0.\n")

while True:
    numero = int(input("Digite um número inteiro: "))


    if numero == 0:
        break


    soma_total += numero

print("-" * 30)
print(f"Programa encerrado! A soma total dos números digitados é: {soma_total}")
print("-" * 30)