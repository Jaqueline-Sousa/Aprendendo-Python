pessoa = {
    "nome": "Jaqueline",
    "idade": 26,
    "cidade": "Sobradinho DF"
}

print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Cidade: {pessoa['cidade']}")


pessoa["idade"] = 27

pessoa["profissão"] = "Estudante de Técnico em Desenvolvimento de sistemas"

print(pessoa)