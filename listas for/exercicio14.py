vendas = [1200.50, 3400.00, 980.00, 5600.20, 2100.00, 850.00]

media_vendas = sum(vendas) / len(vendas)

vendas_acima_da_media = []

for venda in vendas:
    if venda > media_vendas:
        vendas_acima_da_media.append(venda)

print(f"Média de faturamento da equipe: R$ {media_vendas:.2f}")
print(f"Vendas acima da média: {vendas_acima_da_media}")