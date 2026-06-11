carro1 = {
    "marca" : "Chevrolet",
    "modelo" : "Chevete",
    "ano"  : 1198

}

carro2 = {
    "modelo" : "brasília",
    "cor" : "amarelo",
    "placa" : "JPG4021"
}
carro_completo = {**carro2, **carro1} #Cria novo dicionario com os 2 valores
print(carro_completo)

novo_carro = carro1|carro2
print(f"novo carro: {novo_carro}")
print(f"carro completo: {carro_completo}\n")

carro1.update(carro2) #Atualiza dicionario

print(f"carro1 atualizado: {carro1}")