while True:

    print("\n--- Menu de Atendimentos ---")
    entrada = input("Digite o código do produto (ou 'sair' para encerrar): ").strip()

    if entrada.lower() == 'sair':
        print("Programa encerrado. Até logo")
        break


    codigo = int(entrada)


    match codigo:

        case 100:
            print("Cachorro-Quente - R$ 10,00")

        case 101:
            print("Bauru Simples - R$ 12,00")

        case 102:
            print("X-Salada - R$ 15,00")

        case 103:
            print("Hambúrguer - R$ 13,00")

        case _:
            print("Código de produto inválido.")