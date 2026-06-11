lista = ["macarrao", "feijao", "arroz", "feijao", "carne", "miojo", "arroz"]


contador_palavras = {}


for palavra in lista:

    contador_palavras[palavra] = lista.count(palavra)

print(contador_palavras)