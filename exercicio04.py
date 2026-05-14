ano_atual = 2026

ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = ano_atual - ano_nascimento


print(f"\nIdade atual: {idade} anos")

if idade < 18:
    print("Classificação: MENOR de idade.")
elif idade < 60:
    print("Classificação: ADULTO.")
else:
    print("Classificação: IDOSO (+60).")
