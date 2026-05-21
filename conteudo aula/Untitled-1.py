salario_bruto = float(input("Digite o salário bruto do cliente: R$ "))
valor_parcela = float(input("Digite o valor da parcela desejada: R$ "))

limite_maximo = (salario_bruto * 30) / 100

print(f"O limite máximo permitido para a parcela é: R$ {limite_maximo:.2f}")

if valor_parcela <= limite_maximo:
    print("Crédito Aprovado")
else:
    print("Crédito Recusado")
