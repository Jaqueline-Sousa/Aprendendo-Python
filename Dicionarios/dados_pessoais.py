dados_pessoais = {
    "nome" : "Joao",
    "idade" : 21,
    "nascimento" : "20-05-2005",
    "sexo" : "m",
    "altura" : 1.70,
    "temCNH" : True
}

for chave, valor in dados_pessoais.items ():
    print(f"{chave}: {valor}")

print("----------------------------------")

print(dados_pessoais.pop("")