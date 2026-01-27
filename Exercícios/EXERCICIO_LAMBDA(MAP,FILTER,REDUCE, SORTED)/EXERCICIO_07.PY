#Ordenar por último caractere (sorted + lambda)

#Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.


lista = ["banana", "uva", "maçã", "laranja"]

print(sorted(lista, key=lambda x: x[-1]))
