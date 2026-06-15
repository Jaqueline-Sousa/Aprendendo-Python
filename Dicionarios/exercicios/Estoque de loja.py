estoque = {"Teclado": 15, "Mouse": 22, "Monitor": 8}

print(estoque)
atualiza_estoque = False
continuar = "s"
while continuar == "s":

    nome, quantidade = input("Digite o nome do Produto que deseja comprar e a quantidade separados por virgulas: ").split(",")

    for chave, valor in estoque.items():
      if nome.lower() == chave.lower():
              if valor == 0:
                  print("Estoque esgotado!")
                  continue
              if valor < int(quantidade):
                  print("Estoque insuficiente!")
                  continue
      else:
          estoque[chave]  -= int(quantidade)
          atualiza_estoque = True

    if atualiza_estoque:
        print("Estoque atualizado com sucesso!")
        for chave, valor in estoque.items():
            print(f"'{chave}': {valor}")

    continuar = input("Deseja continuar? s/n: ") [0].lower()