produtos = {
    "Notebook": 3500.00,
    "Mouse": 150.00,
    "Teclado": 250.00
}


busca = input("Digite o nome do produto que deseja buscar: ").strip()

produtos_formatados = {k.lower(): v for k, v in produtos.items()}

if busca.lower() in produtos_formatados:
    preco = produtos_formatados[busca.lower()]
    print(f"O preço do produto '{busca}' é R$ {preco:.2f}")
else:
    print("Produto não encontrado")