import time

print("Iniciando a contagem regressiva para a decolagem... ")
print("----------------------------------")


for segundo  in range(10, -1, -1 ):
    print(segundo)

    time.sleep(1)

    print("--------------------------------")

print("Decolar ")