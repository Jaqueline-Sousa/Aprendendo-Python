while True:
    perfil = input("Digite o perfil do usuário: ").strip()

    match perfil.upper():

        case "Admin":
            print("Acesso total: Criar, Ler, Atualizar e Deletar")

        case "Gerente":
            print("Acesso gerencial: Criar, Ler e Atualizar")

        case "Editor":
            print("Acesso de conteúdo: Ler e Atualizar")

        case  "Visitante" :
            print("Acesso restrito: Apenas Leitura")

        case _:
            print("Perfil não reconhecido. Acesso bloqueado")