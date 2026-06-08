estoque = [
    [12, 5, 8],
    [3, 15, 2],
    [19, 0, 7]
]

prateleira = int(input("Digite o numero da prateleira(0 a 2):" ))
divisoria = int(input("Digite o numero da divisoria(0 a 2):" ))


linha = prateleira -1
coluna = divisoria -1

quantidade = estoque[linha][coluna]

print(f"\nNa prateleira {prateleira}, divisória {divisoria}, há {quantidade} caixas.")

