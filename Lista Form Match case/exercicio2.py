while True:

 letra = input("Digite uma letra (ou 'sair' para encerrar): ").strip()

 if letra.lower() == 'sair':
     print("Programa encerrado.")
     break

 match letra.upper():


    case "A":
        letra = "Excelente Trabalho! "
        print(letra)
    case "B":
        letra = "Bom Desempenho! "
        print(letra)
    case "C":
        letra = "Satisfatório! "
        print(letra)
    case "D":
        letra = "Abaixo da média(Atenção)."
        print(letra)
    case "F":
        letra = "Reprovado"
        print(letra)
    case _:
        letra = "Conceito Desconhecido"
        print(letra)

 
