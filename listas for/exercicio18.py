inicial = int(input("Digite o valor inicial: "))
final = int(input("Digite o valor final: "))
passo = int(input("Digite o valor do passo: "))

print(f"\nContagem de {inicial} até {final} de {passo} em {passo}:")


for i in range(inicial, final + 1, passo):
    print(i)