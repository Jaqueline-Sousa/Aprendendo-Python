numero = int(input("Digite um número inteiro para ver sua tabuada: "))

print(f"\nTabuada do {numero}:")
print("-" * 15)


for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

print("-" * 15)