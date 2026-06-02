while True:

    letra = input("Digite uma letra (ou '0' para sair): ").strip().lower()

    match letra.lower():
        case '0':
            break

        case 'a' | 'e' | 'i' | 'o' | 'u':
            print("Você digitou uma VOGAL. ")
         case _:
            print("Consoante")
