while True:

 letra = (input("Digite uma letra: "))

 match letra.lower():


    case "A":
        letra = "Excelente Trabalho! "

    case "B":
        letra = "Bom Desempenho! "

    case "C":
        letra = "Satisfatório"

    case "D":
        letra = "Abaixo da média(Atenção)."

    case "F":
        letra = "Reprovado"

    case _:
        letra = "Conceito Desconhecido"


 
