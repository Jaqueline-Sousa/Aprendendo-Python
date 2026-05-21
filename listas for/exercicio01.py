listaNumeros = []

print("Por favor, digite 6 números inteiros:")
for i in range(1, 7):
    numero = int(input(f"Digite o {i}º número: "))
    listaNumeros.append(numero)
    listaNumeros.sort()

print(listaNumeros)

print("\n--- Resultados ---")

print(f"Soma de todos os valores: {sum(listaNumeros)}")
print(f"Maior valor: {max(listaNumeros)}")
print(f"Menor valor: {min(listaNumeros)}")

