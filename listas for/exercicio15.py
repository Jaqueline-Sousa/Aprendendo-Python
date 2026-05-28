ids_clientes = [101, 102, 103, 101, 104, 102, 105, 106, 103]


ids_unicos = []


for id_cliente in ids_clientes:

    if id_cliente not in ids_unicos:
        ids_unicos.append(id_cliente)


print("Lista original:", ids_clientes)
print("Lista limpa (sem duplicatas):", ids_unicos)