numero = float(input("Digite o 1º número: "))
num = float (input("Digite o 2º número: "))
maior = numero
menor = num

if numero > maior:
    maior = numero
if num < menor:
    menor = num
print(f"\nO MAIOR número digitado foi: {maior}")
print(f"O MENOR número digitado foi: {menor}")

