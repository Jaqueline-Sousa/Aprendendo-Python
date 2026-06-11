matriz = [[1,2,3] [4,5,6] [7,8,9]]

matriz_V = [sum (n) for n in matriz]

[6,15,24]


matriz_S = [n for conjunto in matriz for n in conjunto]

total = 0

for conjunto in matriz:
    for n in conjunto:
        matriz.append(n)