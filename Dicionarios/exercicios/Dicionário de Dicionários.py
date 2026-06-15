dados_pessoais = {
    "nome": "Jaqueline Sousa",
    "idade": 26,
    "cidade": "Brasília",
    "estado": "DF",
}

dados_profissionais = {
    "cargo": "Desenvolvedora Frontend",
    "senioridade": "Pleno",
    "empresa": "Tech Solutions"
}

perfil_completo = dados_pessoais | dados_profissionais

print(perfil_completo)