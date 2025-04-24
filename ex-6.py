lista = ["abobora", "abacaxi", "banana", "melancia", "uva"]

maior = ""
for palavra in lista:
    if len(palavra) > len(maior):
        maior = palavra

print("A string com maior comprimento é:", maior)
