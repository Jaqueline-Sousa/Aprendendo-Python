numeroDia = int(input("Digite um número de 1 a 7:"))


diaSemana=""
match numeroDia:

    case 1:
        diaSemana = "Domingo"

    case 2:
        diaSemana = "Segunda-feira"

    case 3:
        diaSemana = "Terça-feira"

    case 4:
        diaSemana = "Quarta-feira"

    case 5:
        diaSemana = "Quinta-feira"

    case 6:
        diaSemana = "Sexta-feira"

    case 7:
        diaSemana = "Sábado"

    case _:
        diaSemana = "Dia inválido"


print(diaSemana)
