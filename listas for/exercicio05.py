SENHA_CORRETA = "senac123"

acesso_concedido = False

for tentativa in range(1, 4):
    senha_digitada = input(f"Digite sua senha (Tentativa {tentativa}/3): ")

    if senha_digitada == SENHA_CORRETA:
        print("Acesso Permitido")
        acesso_concedido = True
        break
    else:
        print("Senha incorreta!")

        if not acesso_concedido:
            print("Conta Bloqueada")

