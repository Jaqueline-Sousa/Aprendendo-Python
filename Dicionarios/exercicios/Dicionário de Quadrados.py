#quadrados = {x:x**2 for x in range (1,6)}
#print(quadrados)

dicionario_de_quadrados = {}

for i in range(1,6):
    dicionario_de_quadrados.setdefault(i, i**2)
    print(dicionario_de_quadrados)

print("Chave | Valor")
for  k, v in dicionario_de_quadrados.items():
    print(f"{k}: -> {v}")