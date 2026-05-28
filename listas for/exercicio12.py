maiores_18 = 0
total_homens = 0
mulheres_menos_20 = 0

while True:
    print("-" * 30)
    print("    Cadastro de pessoas    ")
    print("-" * 30)

    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
     sexo = str(input("Sexo: [M/F] ")).strip().upper()
    if idade > 18:
        maiores_18 += 1

    if sexo == "M":
        total_homens += 1

    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

        print("-" * 30)
        print("      FIM DO PROGRAMA      ")
        print("-" * 30)
        print(f"Total de pessoas com mais de 18 anos: {maiores_18}")
        print(f"Ao todo, temos {total_homens} homens cadastrados.")
        print(f"E temos {mulheres_menos_20} mulheres com menos de 20 anos.")
