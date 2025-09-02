#Contando frequência de palavras

#Escreva uma função que receba uma lista de palavras
# e retorne um dicionário com a contagem de cada palavra.


def contar_palavra(contar_lista):
    contar = {}

    for palavra in contar_lista:
        if palavra in contar:
            contar[palavra] += 1
        else:
            contar[palavra] = 1
    return contar

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]

total = contar_palavra(palavras)

print(total)