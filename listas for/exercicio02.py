notas = []

for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("Exiba a média" * 30)

if media >= 7.0:
    print(f"Notas do aluno: {notas}")
    print(f"Média: {media:.1f}")
    print("Situação: Aprovado")
else:
    print(f"Notas do aluno: {notas}")
    print(f"Média: {media:.1f}")
    print("Situação: Recuperação")