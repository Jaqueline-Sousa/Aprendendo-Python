matriz_quadrada = [
[5, 2, 9],

[1, 8, 3],

[4, 7, 6]

]

somaDiagonal = 0
for i in range(len(matriz_quadrada)):
    somaDiagonal += matriz_quadrada[i][i]
print(f"A soma é: {somaDiagonal}")
