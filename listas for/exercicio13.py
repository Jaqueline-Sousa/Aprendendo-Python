carrinho = []

print("--- Simulador de Carrinho de Compras ---")
print("Digite o nome do produto para adicionar ou 'sair' para encerrar.\n")

while True:
    produto = input("Digite o nome do produto: ").strip()

    if produto.lower() == 'sair':
        break


    if produto:
        carrinho.append(produto)
        print(f"'{produto}' adicionado ao carrinho!")
    else:
        print("Por favor, digite um nome de produto válido.")

print("\n----------------------------------------")


if carrinho:



    print("Seu carrinho de compras final (Ordem Alfabética):")
    for item in  sorted(carrinho):
        print(f"- {item}")
else:
    print("Seu carrinho está vazio.")