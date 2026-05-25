emails = ["joao@gmail.com", "maria@senac.df", "pedro@outlook.com", "ana@senac.df"]

print("E-mails institucionais encontrados:")
print("-" * 35)

for email in emails:

    if email.endswith("@senac.df"):
        print(email)