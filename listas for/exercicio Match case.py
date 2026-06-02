while True:
    print("Operações:  /n 1 - SOMAR /n 2 - Subtrair /n 3 - Multiplicar  /n 4 - Dividir /n 5 - Sair")


     match opcao:

        case 1:
        result = num1 + num2
         print(f"O resultado é {result}")
        case 2:
        result = num1 - num2
         print(f"O resultado é {result}")
         case 3:
            result = num1 * num2
             print(f"O resultado é {result}")