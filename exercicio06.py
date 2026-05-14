lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if (lado1 + lado2 > lado3) or (lado1 + lado3 > lado2) or (lado2 + lado3 > lado1):
    print("\n Os lados informados formam um triângulo!")
    if lado1 == lado2 == lado3:
        print("Tipo: Equilátero (Todos os lados são iguais).")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("Tipo: Escaleno (Todos os lados são diferentes).")
    else:
        print("Tipo: Isósceles (Dois lados são iguais).")

else:
    print("Tipo: (Não é possível formar um triangulo).")