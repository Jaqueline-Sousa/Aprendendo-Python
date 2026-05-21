for x in range (0,51,5):
    print(x)

    numeros = { 10, 30, 35, 43, 56, 69}

    for x in numeros:
        print (x)

        #Simulando uma chamada


alunos = ["Jaqueline", "Débora", "Evilyn", "Arthur", "Isaac", "Escobar", "Rafael", "Luã", "Lindoso", "Wojcieskovsky"]

alunos.sort()

print(f"Quantos alunos tem na sala: {len(alunos)}")
print("--- Iniciando a chamada! ---")

for i in alunos:
    print(f"Aluno(a) {i} está pressente!")
print ("--- Fim da chamada!---")