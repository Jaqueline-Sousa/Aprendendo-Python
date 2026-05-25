lista_principal = []
pares = []
impares = []

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    lista_principal.append(numero)

for numero in lista_principal:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
 
print("-" * 40)
print(f"Lista Principal: {lista_principal}")
print(f"Lista de Pares:  {pares}")
print(f"Lista de Ímpares: {impares}")