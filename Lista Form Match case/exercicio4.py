while True:
    mes = input("Digite um mes do ano: ").strip()

    if mes.lower() == 'sair':
        print("Programa encerrado. Até logo")
        break


    match mes:

        case "janeiro"|"fevereiro"|"dezembro":
            print("Verão")


        case "março"|"abril"|"maio":
            print("Outono")

        case "junho"|"julho"|"agosto":
            print("Inverno")

        case "setembro"|"outubro"|"novembro":
            print("Primavera")

        case _:
            print("Mes inválido.")