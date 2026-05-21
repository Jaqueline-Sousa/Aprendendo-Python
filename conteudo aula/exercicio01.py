N1 = int (input ("Digite o primeiro número: N "))
N2 = int (input ("Digite o segundo número: N "))
Resultado = N1 // N2  
Resultado2 = N1 % N2  
Resultado3 = N1 ** N2
print ("O resultado da parte inteira da divisão é: ", Resultado)
print ("O resultado2 é o resto da divisão: ", Resultado2)
print ("O resultado3 da potencia é: ", Resultado3)

print ("---------------------------------")
print (" Operadores Relacionados ")
print ("------------------------------------")

Relação1 = N1 > N2
Relação2 = N1 < N2
Relação3 = N1 >= N2
Relação4 = N1 <= N2
Relação5 = N1 == N2
Relação6 = N1 != N2


print ("Os resultados das relações estão a baixo  \n{} \n{} \n{} \n{} \n{} \n{}".format (Relação1, Relação2,Relação3,Relação4, Relação5, Relação6))
