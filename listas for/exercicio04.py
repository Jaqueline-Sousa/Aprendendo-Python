ano_atual = 2026

maiores = 0
menores = 0

for i in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print("-" * 40)
print(f"Total de pessoas que já atingiram a maioridade: {maiores}")
print(f"Total de pessoas que ainda são menores de idade: {menores}")